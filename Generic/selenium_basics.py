from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

URL = r'https://www.makemytrip.com/'
driver_path = r"C:\Users\Meher Kiran\Downloads\chromedriver_win32\chromedriver.exe"
USERNAME = r''
PASSWORD = ''
driver = webdriver.Chrome(driver_path)
driver.get(URL)
driver.maximize_window()


# Github Login
"""getUserElem = driver.find_element_by_name('login')
getPassElem = driver.find_element_by_name('password')
getLoginButton = driver.find_element_by_name('commit')

getUserElem.clear()
getUserElem.send_keys(USERNAME)
getPassElem.clear()
getPassElem.send_keys(PASSWORD)
getLoginButton.click()
#getRepositoryLink = WebDriverWait(driver, 50).until(lambda driver : driver.find_element_by_link_text('Your repositories'))"""



# Gmail Login
"""getUserElem = driver.find_element_by_name('identifier')
getNextButton = driver.find_element_by_id('identifierNext')
getUserElem.clear()
getUserElem.send_keys(USERNAME)
getNextButton.click()
getPassElem = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name('password'))
getPassElem.clear()
getPassElem.send_keys(PASSWORD)
getLoginButton = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('passwordNext'))
getLoginButton.click() """

# Google Search
"""URL = "http://www.google.com"
chrome_driver_path = r"C:\Users\Meher Kiran\Downloads\chromedriver_win32\chromedriver.exe"
chrome_driver = webdriver.Chrome(chrome_driver_path)
chrome_driver.get(URL)
#assert 'Python' in chrome_driver.title

elem = chrome_driver.find_element_by_name('q')
elem.clear()
elem.send_keys('Python Selenium')
elem.send_keys(Keys.RETURN)
time.sleep(5)
chrome_driver.close()"""
