import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xml.etree.ElementTree as ET

class UserLoginLogoutTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

  

    def test_user_login_logout(self):
        login_data_list = self.retrieve_login_data_list('../xml/login_data.xml')

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
            
            # Logout
            logout_link = self.driver.find_element(By.LINK_TEXT, "Log out")
            logout_link.click()
            time.sleep(2)

            # Verify successful logout
            login_link_text = self.driver.find_element(By.LINK_TEXT, "Log in").text
            self.assertEqual(login_link_text, "Log in")

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

if __name__ == "__main__":
    unittest.main()
