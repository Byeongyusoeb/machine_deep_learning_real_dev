'''
Delvelopment environment
 - Ubuntu with below packages
    * Selenium
    * PhantomJS
    * Beautifulsoup4
    * Libfontconfig
    * fonts-nanum*

'''

from selenium import webdriver

url = "http://www.naver.com"

browser = webdriver.PhantomJS() # To extract PhantomJS driver

browser.implicitly_wait(3) # Wait for three second

browser.get(url) # Get URL

browser.save_screenshot("./download/Webstie.png") # Take and save a screenshot

browser.quit() # Quit browser