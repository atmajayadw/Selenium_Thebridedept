#1.Import module
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from colorama import Fore, Style
import time

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
        username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'email')))
        username.send_keys("atmajaya.dw@gmail.com")

        # Find and input Password field
        password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password')))
        password.send_keys("jay123")
        
        # Find and Click CTA Login
        login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/section/div/div/div[2]/div[5]/button')))
        login.click()
        print(Fore.GREEN + 'Sukses Login!')
        print(Fore.YELLOW + 'Making new transaction')
        print(Style.RESET_ALL)  

        # Validating login
        try:
            # Validationg invalid login creds 
            validation_login = WebDriverWait(driver, 5).until(
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

            # Access Dashboard page & Assert
            assert "Atmajaya" in profile.text

        try:
            # Find and Click menu Store
            time.sleep(1)
            menu_store = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div[5]'))) #gapake login
            menu_store.click()

            # Find and Click CTA Store    
            btn_store = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div[6]/div/div/div[1]/div[3]/a')))
            btn_store.click()

            # Find and Click Product
            select_product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/section[2]/div/div[2]/div/div[5]/div[2]/a/div')))
            select_product.click()

            # Show Product Detail page, Find CTA and Click CTA BUY   
            show_product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/section/div/div[3]/div[2]/div/div[6]/button')))
            show_product.click()

            # Find and Select Date
            select_date = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/section/div[2]/div/div/div[3]/div[1]/div/div[2]/div/div[2]/div[6]/div[4]/div')))
            select_date.click()

            # Find CTA and Click CTA Buy/Submit & Show Xendit Page
            buy = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/section/div[2]/div/div/div[4]/button')))
            buy.click()

            # Print / show Result
            time.sleep(5)
            print(Fore.GREEN + 'Success to create new transaction')
            print(Style.RESET_ALL)
        except: 
            print(Fore.RED + 'Failed to create new transaction')
            print(Style.RESET_ALL)

    #5.End session / close browser
    def tearDown(self):
        self.driver.close()
        
#6.Running Test
if __name__ == "__main__":
    unittest.main()