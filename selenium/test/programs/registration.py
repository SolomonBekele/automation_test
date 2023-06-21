import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import xml.etree.ElementTree as ET

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        registration_data_list = self.retrieve_registration_data_list('../xml/registration_data.xml')

        for registration_data in registration_data_list:
            # Navigate to the home page
            self.driver.get("http://demowebshop.tricentis.com")
            time.sleep(2)

            # Go to the registration page
            register_link = self.driver.find_element(By.LINK_TEXT, "Register")
            register_link.click()
            time.sleep(2)

            # Fill in the registration form
            gender_radio = self.driver.find_element(By.ID, "gender-" + registration_data['gender'])
            gender_radio.click()
            time.sleep(1)

            first_name_input = self.driver.find_element(By.ID, "FirstName")
            first_name_input.send_keys(registration_data['firstName'])
            time.sleep(1)

            last_name_input = self.driver.find_element(By.ID, "LastName")
            last_name_input.send_keys(registration_data['lastName'])
            time.sleep(1)

            email_input = self.driver.find_element(By.ID, "Email")
            email_input.send_keys(registration_data['email'])
            time.sleep(1)

            password_input = self.driver.find_element(By.ID, "Password")
            password_input.send_keys(registration_data['password'])
            time.sleep(1)

            confirm_password_input = self.driver.find_element(By.ID, "ConfirmPassword")
            confirm_password_input.send_keys(registration_data['confirmPassword'])
            time.sleep(1)

            # Submit the form
            register_button = self.driver.find_element(By.CSS_SELECTOR, '[type="submit"][value="Register"]')
            register_button.click()
            time.sleep(2)

            # Verify successful registration
            registration_confirmation = self.driver.find_element(By.CSS_SELECTOR, ".result").text
            self.assertEqual(registration_confirmation, "Your registration completed")

    def retrieve_registration_data_list(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        registration_data_list = []

        for registration_data in root.findall('registration'):
            data = {}
            for element in registration_data:
                data[element.tag] = element.text
            registration_data_list.append(data)

        return registration_data_list

if __name__ == "__main__":
    unittest.main()
