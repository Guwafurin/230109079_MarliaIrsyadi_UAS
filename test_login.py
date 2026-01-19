from utils.driver import get_driver
from pages.login_page import LoginPage
import time

print("STEP 1: Memulai driver")
driver = get_driver()

print("STEP 2: Membuka website")
driver.get("https://www.demoblaze.com")

login = LoginPage(driver)
print("STEP 3: Melakukan login")
login.login("testuser", "testpass")

time.sleep(5)
driver.quit()
print("SELESAI")
