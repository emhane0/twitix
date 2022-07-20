from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os
import time

torexe = os.popen(r'C:\Users\ethan\Desktop\Tor Browser\Browser\TorBrowser\Tortor.exe')
profile = FirefoxProfile(r'C:\Users\ethan\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser')
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)
profile.set_preference("network.proxy.socks_remote_dns", False)
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile= profile, executable_path=r'geckodriver.exe')
driver.get("http://check.torproject.org")
time.sleep(10)