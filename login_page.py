from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, user, pwd):
        self.driver.find_element(By.ID, "login2").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "loginusername").send_keys(user)
        self.driver.find_element(By.ID, "loginpassword").send_keys(pwd)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
