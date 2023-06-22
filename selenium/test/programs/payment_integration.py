import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import xml.etree.ElementTree as ET

class UserLoginShoppingCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_user_login_shopping_cart(self):
        login_data = self.retrieve_login_data('../xml/login_data.xml')
        product_data_list = self.retrieve_product_data_list('../xml/product_data.xml')
        payment_data = self.retrieve_payment_data('../xml/payment.xml')

        # Navigate to the home page
        self.driver.get("http://demowebshop.tricentis.com")
        time.sleep(2)

        # Go to the login page
        login_link = self.driver.find_element(By.LINK_TEXT, "Log in")
        login_link.click()
        time.sleep(2)

        # Fill in the login form
        email_input = self.driver.find_element(By.ID, "Email")
        email_input.send_keys(login_data['email'])
        time.sleep(1)

        password_input = self.driver.find_element(By.ID, "Password")
        password_input.send_keys(login_data['password'])
        time.sleep(1)

        # Submit the login form
        login_button = self.driver.find_element(By.CSS_SELECTOR, '[type="submit"][value="Log in"]')
        login_button.click()
        time.sleep(2)

        # Verify successful login

        # Add items to the shopping cart
        for product_data in product_data_list:
            self.add_to_cart(product_data['product_name'])

        # View shopping cart
        cart_link = self.driver.find_element(By.CSS_SELECTOR, '.cart-qty')
        cart_link.click()
        time.sleep(2)

        # Verify items in the shopping cart
        terms_checkbox = self.driver.find_element(By.ID, 'termsofservice')
        self.driver.execute_script("arguments[0].click();", terms_checkbox)
        time.sleep(1)

        # Proceed to checkout
        checkout_button = self.driver.find_element(By.CSS_SELECTOR, '.checkout-button')
        checkout_button.click()
        time.sleep(2)

        # Fill in payment details
        # card_number_input = self.driver.find_element(By.ID, 'CardNumber')
        # card_number_input.send_keys(payment_data['card_number'])
        # time.sleep(1)

        # expiration_month_input = self.driver.find_element(By.ID, 'ExpireMonth')
        # expiration_month_input.send_keys(payment_data['expiration_month'])
        # time.sleep(1)

        # expiration_year_input = self.driver.find_element(By.ID, 'ExpireYear')
        # expiration_year_input.send_keys(payment_data['expiration_year'])
        # time.sleep(1)

        # cvv_input = self.driver.find_element(By.ID, 'CardCode')
        # cvv_input.send_keys(payment_data['cvv'])
        # time.sleep(1)

        # Check the terms of service checkbox
       

        # Place the order
        # place_order_button = self.driver.find_element(By.CSS_SELECTOR, '[value="Place Order"]')
        # place_order_button.click()
        # time.sleep(2)

        # Verify successful order placement

        # Fill in billing address details
        company_input = self.driver.find_element(By.ID, 'BillingNewAddress_Company')
        company_input.send_keys("Test Company")
        time.sleep(1)



        country_dropdown = self.driver.find_element(By.ID, 'BillingNewAddress_CountryId')
        country_dropdown.click()
        time.sleep(1)

# Locate and click the desired option by text
        option_usa = self.driver.find_element(By.XPATH, '//option[text()="United States"]')
        option_usa.click()
        time.sleep(1)

        city_input = self.driver.find_element(By.ID, 'BillingNewAddress_City')
        city_input.send_keys("Test City")
        time.sleep(1)

        address1_input = self.driver.find_element(By.ID, 'BillingNewAddress_Address1')
        address1_input.send_keys("Test Address 1")
        time.sleep(1)

        address2_input = self.driver.find_element(By.ID, 'BillingNewAddress_Address2')
        address2_input.send_keys("Test Address 2")
        time.sleep(1)

        zip_input = self.driver.find_element(By.ID, 'BillingNewAddress_ZipPostalCode')
        zip_input.send_keys("12345")
        time.sleep(1)

        phone_input = self.driver.find_element(By.ID, 'BillingNewAddress_PhoneNumber')
        phone_input.send_keys("1234567890")
        time.sleep(1)

        fax_input = self.driver.find_element(By.ID, 'BillingNewAddress_FaxNumber')
        fax_input.send_keys("9876543210")
        time.sleep(1)

        # Continue to the next step
        continue_button = self.driver.find_element(By.CSS_SELECTOR, '[value="Continue"]')
        continue_button.click()
        time.sleep(2)

        # Verify successful address submission

        # Proceed to the next step (shipping method)
        continue_button = self.driver.find_element(By.CSS_SELECTOR, '[value="Continue"]')
        continue_button.click()
        time.sleep(2)

        # Verify successful shipping method selection

        # Proceed to the next step (shipping method)
       

        # Place the order
        place_order_button = self.driver.find_element(By.CSS_SELECTOR, '[value="Place Order"]')
        place_order_button.click()
        time.sleep(2)

        # Verify successful order placement

        # Logout
        logout_link = self.driver.find_element(By.LINK_TEXT, "Log out")
        logout_link.click()
        time.sleep(2)

        # Verify successful logout


    def add_to_cart(self, product_name):
        search_input = self.driver.find_element(By.NAME, "q")
        search_input.clear()
        search_input.send_keys(product_name)
        time.sleep(1)

        search_button = self.driver.find_element(By.CSS_SELECTOR, '[type="submit"][value="Search"]')
        search_button.click()
        time.sleep(2)

        add_to_cart_button = self.driver.find_element(By.CSS_SELECTOR, '.product-box-add-to-cart-button')
        add_to_cart_button.click()
        time.sleep(2)

    def retrieve_login_data(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        login_data = {}
        login_node = root.find('login')
        for element in login_node:
            login_data[element.tag] = element.text

        return login_data

    def retrieve_product_data_list(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        product_data_list = []
        for product_data in root.findall('product'):
            data = {}
            for element in product_data:
                data[element.tag] = element.text
            product_data_list.append(data)

        return product_data_list

    def retrieve_payment_data(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        payment_data = {}
        payment_node = root.find('payment')
        for element in payment_node:
            payment_data[element.tag] = element.text

        return payment_data

if __name__ == "__main__":
    unittest.main()
