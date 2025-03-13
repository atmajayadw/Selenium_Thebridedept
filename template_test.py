# 1. Import module
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from colorama import Fore, Style

# 2. Create test module
class sampletest(unittest.TestCase):
    
    # 3. Initialization
    def setUp(self):
        self.driver = webdriver.Chrome()

    # 4. Test scenario
    def test_open_page(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("Python")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    # 5. End session / close browser
    def tearDown(self):
        self.driver.close()

# 6. Running Test
if __name__ == "__main__":
    unittest.main()
