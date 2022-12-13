from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

import sys
import json
import customer as CUS

#################################################################
# Status -- 12/4/2022
#
# Finished:
#
# Add a customer --
#
#   @app.post('/adduser/{id}')
#   async def AddUser(id: int, user: User):
#
# It added a user to the database.
#
# Not Finished:
#
# Update a customer --
#
#   @app.put('/update/{id}')
#   async def UpdateUser(id: int, user: User):
#
#################################################################


class User(BaseModel):
    ID: int = None
    firstName: str = None
    lastName: str = None
    houseNo: str = None
    street: str = None
    city: str = None
    state: str = None
    zipCode: str = None
    phoneNo: str = None
    email: str = None


app = FastAPI()


def GetAllCustomers():
    # Connect to the DB
    CUS.ConnectDB()
    # Execute the SELECT *
    CUS.myCursor.execute(CUS.selectAll)

    # Create and save the list of all customers
    CUS.CreateAllCustomers(CUS.myCursor)

    # The list of all customers in the database
    global allCustomers

    allCustomers = CUS.listCustomers

    # Disconnect/close the DB connection
    CUS.DisconnectDB()


def VerifyCustomer(id):
    GetAllCustomers()

    for cus in allCustomers:
        if cus[0][0] == id:  # The first field is the ID
            return True  # The customer with this id is found

    return False        # The customer with this id is not found

#################################################################
# GET
#################################################################

# Root/home page


@app.get('/')
async def Home():

    # GetAllCustomers()
    # return allCustomers[0][0]

    return {'Message': 'Hello, World!'}


# Get all the customers

@app.get('/users')
async def GetUsers():
    GetAllCustomers()
    return allCustomers


# Get a customer by his/her ID

@app.get('/users/{id}')
async def GetUserByID(id: int):
    # SELECT * from customer WHERE customer_id = id;

    # Connect to the DB
    CUS.ConnectDB()

    CUS.myCursor.execute(
        'SELECT * FROM customer WHERE customer_id = %s', (id,))

    oneUser = CUS.myCursor.fetchone()

    # Disconnect/close the DB connection
    CUS.DisconnectDB()

    return oneUser


# Get the customer by his/her first or last name

@app.get('/userbyname/{name}')
async def GetUserByName(name: str):
    # Get all the users/customers from the database.
    # and store them in allCustomers
    GetAllCustomers()

    for customer in allCustomers:
        if customer[1].lower() == name.lower() or customer[2].lower() == name.lower():
            return customer

    return 'User is not found!!!'


#################################################################
# PUT - Update a customer with the provided fields.
#################################################################

# UPDATE statement
'''
updateSQL = 'UPDATE customer SET \
                first_name = %s, \
                last_name = %s, \
                house_no = %s, \
                street = %s,\
                city = %s, \
                state = %s, \
                zip_code = %s, \
                phone_no = %s, \
                email = %s \
                WHERE customer_id = %s'

cursor.execute(updateSQL, (valStr))
'''


@app.put('/update/{id}')
async def UpdateUser(id: int, user: User):
    user.ID = id

    return user


#################################################################
# POST - Create a new customer and add it to the database.
#################################################################


@app.post('/adduser/{id}')
async def AddUser(id: int, user: User):
    insertSQL = 'INSERT INTO customer(customer_id, first_name, last_name, house_no, street, city, state, zip_code, phone_no, email) \
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    user.ID = id

    # Connect to the DB
    CUS.ConnectDB()

    CUS.myCursor.execute(insertSQL,
                         (user.ID, user.firstName, user.lastName, user.houseNo, user.street,
                          user.city, user.state, user.zipCode, user.phoneNo, user.email))

    # Commit the transaction to the database.
    CUS.mydb.commit()


#################################################################
# DELETE
#################################################################

@app.delete('/deleteuser/{id}')
async def DeleteUser(id: int):
    if not VerifyCustomer(id):
        return ('User is not found!!!')

    # DELETE statement:
    # by ID
    delIDSQL = 'DELETE FROM customer WHERE customer_id = %s'

    # Connect to the DB
    CUS.ConnectDB()

    CUS.myCursor.execute(delIDSQL, (id,))

    # Commit the DELETE
    CUS.mydb.commit()

    return userFound


@app.delete('/deleteuserbyname/{name}')
async def DeleteUser(name: str):
    userFound = VerifyCustomer(name)
    if userFound == None:
        return ('User is not found!!!')

    # DELETE statements:
    # by name
    delNameSQL = 'DELETE FROM customer WHERE first_name = %s or last_name = %s'

    # Connect to the DB
    CUS.ConnectDB()

    CUS.myCursor.execute(delNameSQL, (name, name))

    # Commit the DELETE
    CUS.mydb.commit()

    return userFound
