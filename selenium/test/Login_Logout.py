import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class UserLoginLogoutTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()  # Use the appropriate web driver for your browser
        self.driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

    def tearDown(self):
        self.driver.quit()  # Close the browser after each test

    def test_user_login_logout(self):
        # Navigate to the home page
        self.driver.get("http://demowebshop.tricentis.com")
        time.sleep(2)  # Pause for 2 seconds

        # Go to the login page
        login_link = self.driver.find_element(By.LINK_TEXT, "Log in")
        login_link.click()
        time.sleep(2)  # Pause for 2 seconds

        # Fill in the login form
        email_input = self.driver.find_element(By.ID, "Email")
        email_input.send_keys("sool@example.com")
        time.sleep(1)  # Pause for 1 second

        password_input = self.driver.find_element(By.ID, "Password")
        password_input.send_keys("password123")
        time.sleep(1)  # Pause for 1 second

        # Submit the login form
        login_button = self.driver.find_element(By.CSS_SELECTOR, '[type="submit"][value="Log in"]')
        login_button.click()
        time.sleep(2)  # Pause for 2 seconds

        

        # Logout
        logout_url = self.driver.find_element(By.CSS_SELECTOR, '[href="/logout"]').get_attribute("href")
        self.driver.get(logout_url)
        time.sleep(2)  # Pause for 2 seconds

      

if __name__ == "__main__":
    unittest.main()
