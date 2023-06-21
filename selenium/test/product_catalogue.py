import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ProductCatalogueTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()  # Use the appropriate web driver for your browser
        self.driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

    def tearDown(self):
        self.driver.quit()  # Close the browser after each test

    def test_product_catalogue_browsing(self):
        # Navigate to the home page
        self.driver.get("http://demowebshop.tricentis.com")
        time.sleep(2)  # Pause for 2 seconds

        # Click on the "Books" category link
        books_category_link = self.driver.find_element(By.LINK_TEXT, "Books")
        books_category_link.click()
        time.sleep(2)  # Pause for 2 seconds

        # Select a product
        # Select a product
        product_link = self.driver.find_element(By.CSS_SELECTOR, 'h2.product-title > a')
        product_link.click()
        time.sleep(2)  # Pause for 2 seconds


        # Add the product to cart
        add_to_cart_button = self.driver.find_element(By.CSS_SELECTOR, '[value="Add to cart"]')
        add_to_cart_button.click()
        time.sleep(2)  # Pause for 2 seconds


if __name__ == "__main__":
    unittest.main()
