import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class UserRegistrationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()  # Use the appropriate web driver for your browser
        self.driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

    def tearDown(self):
        self.driver.quit()  # Close the browser after each test

    def test_user_registration(self):
        # Navigate to the home page
        self.driver.get("http://demowebshop.tricentis.com")
        time.sleep(2)  # Pause for 2 seconds

        # Go to the registration page
        register_link = self.driver.find_element(By.LINK_TEXT, "Register")
        register_link.click()
        time.sleep(2)  # Pause for 2 seconds

        # Fill in the registration form
        gender_radio = self.driver.find_element(By.ID, "gender-male")
        gender_radio.click()
        time.sleep(1)  # Pause for 1 second

        first_name_input = self.driver.find_element(By.ID, "FirstName")
        first_name_input.send_keys("John")
        time.sleep(1)  # Pause for 1 second

        last_name_input = self.driver.find_element(By.ID, "LastName")
        last_name_input.send_keys("Doe")
        time.sleep(1)  # Pause for 1 second

        email_input = self.driver.find_element(By.ID, "Email")
        email_input.send_keys("sol@example.com")
        time.sleep(1)  # Pause for 1 second

        password_input = self.driver.find_element(By.ID, "Password")
        password_input.send_keys("password123")
        time.sleep(1)  # Pause for 1 second

        confirm_password_input = self.driver.find_element(By.ID, "ConfirmPassword")
        confirm_password_input.send_keys("password123")
        time.sleep(1)  # Pause for 1 second

        # Submit the form
        register_button = self.driver.find_element(By.CSS_SELECTOR, '[type="submit"][value="Register"]')
        register_button.click()
        time.sleep(2)  # Pause for 2 seconds

        # Verify successful registration
        registration_confirmation = self.driver.find_element(By.CSS_SELECTOR, ".result").text
        self.assertEqual(registration_confirmation, "Your registration completed")

if __name__ == "__main__":
    unittest.main()
