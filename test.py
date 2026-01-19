from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(
    "D:/Mata Kuliah/Semester 5/Pengujian Perangkat Lunak/Praktikum/selenium-test/chromedriver.exe"
)

driver = webdriver.Chrome(service=service)
driver.get("https://www.demoblaze.com")
