import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xml.etree.ElementTree as ET

class ShoppingCartTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_shopping_cart(self):
        product_data = self.retrieve_product_data('../xml/pproduct_data.xml')

        # Navigate to the home page
        self.driver.get("http://demowebshop.tricentis.com")
        time.sleep(2)

        # Add products to the cart
        for product in product_data:
            self.add_product_to_cart(product)
            time.sleep(2)

        # Go to the shopping cart
        cart_link = self.driver.find_element(By.CSS_SELECTOR, '[class="cart-label"]')
        cart_link.click()
        time.sleep(2)

        # Verify the added products in the shopping cart

    def add_product_to_cart(self, product):
        product_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, product['name'])
        product_link.click()
        time.sleep(2)

        add_to_cart_button = self.driver.find_element(By.CSS_SELECTOR, '[value="Add to cart"]')
        add_to_cart_button.click()

    def retrieve_product_data(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        product_data = []
        for element in root.findall('product'):
            product = {
                'name': element.find('name').text,
                # Add more product details as needed
            }
            product_data.append(product)

        return product_data

if __name__ == "__main__":
    unittest.main()
