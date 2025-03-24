#1.Import module
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from colorama import Fore, Style

#2.Create test module
class logintest(unittest.TestCase):

    #3.Initialization
    def setUp(self):
        self.driver = webdriver.Chrome()

    #4.Test scenario
    def test_logintest(self):
        driver = self.driver
        driver.maximize_window()

        # Visit Website
        driver.get("https://thebridedept.com/")

        # Click CTA Member
        driver.find_element(By.LINK_TEXT, 'Member').click()

        # Find and input Email field
        username = driver.find_element(By.NAME, 'email')
        username.send_keys("atmajaya.dw@gmail.com")

        # Find and input Password field
        password = driver.find_element(By.NAME, 'password')
        password.send_keys("jay1235")
        
        # Find and Click CTA Login
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/section/div/div/div[2]/div[5]/button')))
        element.click()

        # Validating login
        try:
            # Validationg invalid login creds 
            validation_login = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/section/div/div/div[2]/div[3]/div')))
            print(validation_login.text)
            assert "Invalid email or password" in validation_login.text

            # Print / show Result
            print(Fore.RED + 'Fail! - ' + validation_login.text)
            print(Style.RESET_ALL)
        except: 
            # Validationg success login creds & Access Profile page
            profile = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div[3]/div/span/a')))
            profile.click()

            # Access Dashboard page & Assert
            dashboard = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/div[2]/section/div/div[1]/div/div[1]/div')))
            assert "Latest articles you might like" in dashboard.text
            
            # Print / show Result
            print(Fore.GREEN + 'Sukses Login!')

            # CLick Logout
            logout = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div/div[5]/button')))
            logout.click()

            # Print / show Result
            print(Fore.YELLOW + 'Checking for logout')
            print(Style.RESET_ALL)
            
            # Access Homepage & Assert
            validation_logout = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/section/div/div/div[2]/div[2]')))
            assert "Login As Member" in validation_logout.text

            # Print / show Result
            print(Fore.GREEN + 'Sukses Logout!')
            print(Style.RESET_ALL)

    #5.End session / close browser
    def tearDown(self):
        self.driver.close()

#6.Running Test
if __name__ == "__main__":
    unittest.main()