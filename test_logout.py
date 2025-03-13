import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from colorama import Fore, Style

class logintest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_logintest(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://thebridedept.com/")
        driver.find_element(By.LINK_TEXT, 'Member').click()
        username = driver.find_element(By.NAME, 'email')
        username.send_keys("atmajaya.dw@gmail.com")
        password = driver.find_element(By.NAME, 'password')
        password.send_keys("jay1235")
        
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/section/div/div/div[2]/div[5]/button')))
        element.click()

        try:
            validation_login = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/section/div/div/div[2]/div[3]/div')))
            print(validation_login.text)
            assert "Invalid email or password" in validation_login.text
            print(Fore.RED + 'Fail! - ' + validation_login.text)
            print(Style.RESET_ALL)
        except: 
            profile = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div[3]/div/span/a')))
            profile.click()

            dashboard = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/div[2]/section/div/div[1]/div/div[1]/div')))

            assert "Latest articles you might like" in dashboard.text
            print(Fore.GREEN + 'Sukses Login!')

            logout = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div/div[5]/button')))
            logout.click()

            print(Fore.YELLOW + 'Checking for logout')
            print(Style.RESET_ALL)

            validation_logout = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/section/div/div/div[2]/div[2]')))
            assert "Login As Member" in validation_logout.text
            print(Fore.GREEN + 'Sukses Logout!')
            print(Style.RESET_ALL)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()