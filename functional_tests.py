__author__ = 'Angel_Luis'

'''
Date = '8/2/15'
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Hello World'in browser.title, True
browser.implicitly_wait(3)
#time.sleep(5)
browser.quit()

