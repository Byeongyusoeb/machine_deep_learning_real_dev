'''
For collecting after Javascript code, for sure you use selenium and phantomJS
'''
from selenium import webdriver


# Login process

url = "https://nid.naver.com/nidlogin.login"

browser = webdriver.PhantomJS() # To extract PhantomJS driver

browser.implicitly_wait(3) # Wait for three second

browser.get(url) # Get URL

element_id = browser.find_element_by_id('id') # id input box
element_id.clear()
element_id.send_keys('<ID>')

element_pw = browser.find_element_by_id('pw') # pw input box
element_pw.clear()
element_pw.send_keys('<PW>')

submit_button = browser.find_element_by_css_selector('input.btn_global[type=submit]')
submit_button.submit() # Do submit

browser.save_screenshot('./download/website_login.png')


# Get subjects of mails

url = "https://mail.naver.com"

browser.get(url) # Get URL

browser.save_screenshot('./download/website_mail_list.png')

titles = browser.find_elements_by_css_selector('strong.mail_title')

for title in titles:
    print("- ", title.text)

browser.quit() # Quit browser