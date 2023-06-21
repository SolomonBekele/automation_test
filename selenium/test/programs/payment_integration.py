import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xml.etree.ElementTree as ET

class PaymentIntegrationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_payment_process(self):
        payment_data = self.retrieve_payment_data('../xml/payment_data.xml')

        # Navigate to the home page
        self.driver.get("http://demowebshop.tricentis.com")
        time.sleep(2)

        # Add a product to the cart
        add_to_cart_button = self.driver.find_element(By.CSS_SELECTOR, '[data-productid="1"] [type="button"][value="Add to cart"]')
        add_to_cart_button.click()
        time.sleep(2)

        # Go to the shopping cart
        cart_link = self.driver.find_element(By.CSS_SELECTOR, '[class="cart-label"]')
        cart_link.click()
        time.sleep(2)

        # Proceed to checkout
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
        time.sleep(2)

        # Fill in the billing information
        billing_firstname = self.driver.find_element(By.ID, "BillingNewAddress_FirstName")
        billing_firstname.send_keys(payment_data['firstname'])
        time.sleep(1)

        billing_lastname = self.driver.find_element(By.ID, "BillingNewAddress_LastName")
        billing_lastname.send_keys(payment_data['lastname'])
        time.sleep(1)

        billing_email = self.driver.find_element(By.ID, "BillingNewAddress_Email")
        billing_email.send_keys(payment_data['email'])
        time.sleep(1)

        billing_country = self.driver.find_element(By.ID, "BillingNewAddress_CountryId")
        billing_country.send_keys(payment_data['country'])
        time.sleep(1)

        # ... Fill in the remaining billing information ...

        # Proceed to payment method selection
        continue_payment_button = self.driver.find_element(By.CSS_SELECTOR, '[class="new-payment-method-next-step-button"]')
        continue_payment_button.click()
        time.sleep(2)

        # Select payment method (e.g., Credit Card)
        payment_method = self.driver.find_element(By.ID, "paymentmethod_1")
        payment_method.click()
        time.sleep(1)

        # ... Fill in the credit card details ...

        # Place the order
        place_order_button = self.driver.find_element(By.CSS_SELECTOR, '[class="payment-info-next-step-button"]')
        place_order_button.click()
        time.sleep(2)

        # Verify successful order placement
        order_confirmation = self.driver.find_element(By.CSS_SELECTOR, ".order-completed").text
        self.assertEqual(order_confirmation, "Your order has been successfully processed!")

    def retrieve_payment_data(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        data = {}
        for element in root.findall('payment'):
            data['firstname'] = element.find('firstname').text
            data['lastname'] = element.find('lastname').text
            data['email'] = element.find('email').text
            data['country'] = element.find('country').text
            # Add more data as needed

        return data

if __name__ == "__main__":
    unittest.main()
