from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get('https://www.instagram.com/accounts/emailsignup/')
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[2]").click()