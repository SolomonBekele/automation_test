import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xml.etree.ElementTree as ET

class UserLoginShoppingCartTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_user_login_shopping_cart(self):
        login_data_list = self.retrieve_login_data_list('../xml/login_data.xml')
        product_data_list = self.retrieve_product_data_list('../xml/product_data.xml')

        for login_data in login_data_list:
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


            # Logout
            logout_link = self.driver.find_element(By.LINK_TEXT, "Log out")
            logout_link.click()
            time.sleep(2)


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

    def retrieve_login_data_list(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        login_data_list = []
        for login_data in root.findall('login'):
            data = {}
            for element in login_data:
                data[element.tag] = element.text
            login_data_list.append(data)

        return login_data_list

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

if __name__ == "__main__":
    unittest.main()
