import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xml.etree.ElementTree as ET

class ProductCatalogTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    # def tearDown(self):
    #     self.driver.quit()

    def test_product_search(self):
        product_data = self.retrieve_product_data('../xml/product_data.xml', 'product_search')

        # Navigate to the home page
        self.driver.get("http://demowebshop.tricentis.com")
        time.sleep(2)

        # Search for a product
        search_input = self.driver.find_element(By.ID, "small-searchterms")
        search_input.send_keys(product_data['search_term'])
        time.sleep(1)

        search_button = self.driver.find_element(By.CSS_SELECTOR, '[type="submit"][value="Search"]')
        search_button.click()
        time.sleep(2)

        # Verify search results
        product_list = self.driver.find_elements(By.CSS_SELECTOR, ".product-item .product-title")
        self.assertTrue(len(product_list) > 0)

        # Select a product
        product_link = product_list[0].find_element(By.TAG_NAME, "a")
        product_link.click()
        time.sleep(2)

        # Verify product details page
        

    def test_product_category_navigation(self):
        category_data = self.retrieve_product_data('../xml/product_data.xml', 'product_category')

        # Navigate to the home page
        self.driver.get("http://demowebshop.tricentis.com")
        time.sleep(2)

        # Navigate to a product category
        category_link = self.driver.find_element(By.LINK_TEXT, category_data['category'])
        category_link.click()
        time.sleep(2)


        # Select a product from the category
        product_list = self.driver.find_elements(By.CSS_SELECTOR, ".product-item .product-title")
        self.assertTrue(len(product_list) > 0)

        product_link = product_list[0].find_element(By.TAG_NAME, "a")
        product_link.click()
        time.sleep(2)

        # Verify product details page
        

    def retrieve_product_data(self, xml_file, test_type):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        data = {}
        for item in root.findall(test_type):
            for element in item:
                data[element.tag] = element.text

        return data

if __name__ == "__main__":
    unittest.main()
