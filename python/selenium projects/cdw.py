from nturl2path import url2pathname
from selenium import webdriver

# for finding elements with By.ID, ...
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

import time


def SetUp():
    global driver, url, uname, pw

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome()
    driver = webdriver.Firefox()

    uname = "henryvangard"
    pw = "xxxxxx"

    url = 'https://www.cdw.com/accountcenter/LogOn?target=%2F'

    driver.implicitly_wait(30)  # This is very important to allow ...


def LogIn():
    driver.get(url)
    driver.find_element(By.ID, 'UserName').send_keys(uname)
    driver.find_element('id', 'UserPassword').send_keys(pw)
    driver.find_element('id', 'LogOnButton').click()
    driver.maximize_window()


def SearchItem(item):
    # search for hp products
    driver.find_element(By.ID, 'search-input').send_keys(item)
    # press Enter to search
    driver.find_element(By.ID, 'gh-header-button-search').send_keys(Keys.ENTER)


def AddToCart():
    # add to cart
    driver.find_element('id', 'AddItemToCartStickyHeader').click()


def ReadInFile():
    pass


def Checkout():
    fn = 'John'
    ln = 'Lee'
    co = 'Lee, Inc.'
    street = '121 3rd St'
    city = 'NYC'
    st = 'NY'
    zip = '00215'
    phone = '111-222-3344'

    driver.find_element(
        'id', 'ShippingAddressEditor_AttentionFirstName').send_keys(fn)
    driver.find_element(
        'id', 'ShippingAddressEditor_AttentionLastName').send_keys(ln)
    driver.find_element(
        'id', 'ShippingAddressEditor_CompanyName').send_keys(co)
    driver.find_element(
        'id', 'ShippingAddressEditor_Address1').send_keys(street)
    driver.find_element('id', 'ShippingAddressEditor_City').send_keys(city)

    # drop box implementation

    driver.find_element(
        'id', 'ShippingAddressEditor_ZipOrPostalCode').send_keys(zip)

    driver.find_element('id', 'ShippingAddressEditor_Phone').send_keys(phone)

    # Click on Continue
    driver.find_element('name', 'SubmitType').click()


# Start of app

SetUp()
LogIn()

item = 6914736
SearchItem(item)
AddToCart()

item = 7015784
SearchItem(item)
AddToCart()

item = 6826046
SearchItem(item)
AddToCart()

# check out
# driver.find_element('id', 'expressCheckout').click()

# The checkout form
# Checkout()

####################################################
# Next Phase:
#
# read from file
# add each item to cart while NOT eof
# eof - check out
# fill out check out form
# click Continue
#####################################################

# driver.quit()
