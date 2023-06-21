from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")

# search_box = driver.find_element("name","q")
# search_box.send_keys("Selenium")
# search_box.send_keys(Keys.RETURN)

# btnK = driver.find_element("name","btnK")
# btnK.send_keys(Keys.RETURN)

# time.sleep(20)
# driver.quit()

print(driver.title)
print(driver.current_url)