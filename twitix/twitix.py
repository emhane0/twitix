from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import socket
import socks
from urllib.request import urlopen
from stem import Signal
from stem.control import Controller
from selenium.webdriver.firefox.service import Service

os.startfile(r'C:/Users/ethan/Desktop/Tor Browser/Browser/firefox.exe')

controller = Controller.from_port(port=9151)

def connectTor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150, True)
    socket.socket = socks.socksocket

def renewTor():
    controller.authenticate("abc123")
    controller.signal(Signal.NEWNYM)

def showIP():
    print(urlopen('http://icanhazip.com').read())

for i in range(5):
    renewTor()
    connectTor()
    showIP()
    time.sleep(10)


driver = webdriver.Firefox(service= Service(r'geckodriver.exe'))

driver.get('https://www.instagram.com/accounts/emailsignup/')
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[2]").click()