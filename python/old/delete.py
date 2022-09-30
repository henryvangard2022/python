# this is the customer module which manipulates the 'customer' table of the  MySQL database 'customercrm'
import customer as CUS


#####################################################
# DELETE SQL command implemented as separate module #
#####################################################

delSQL = 'DELETE FROM customer WHERE customer_id = %s'
