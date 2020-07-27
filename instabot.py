
from time import sleep

from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

# login_link = browser.find_element_by_xpath("//a[text()='Log In']")
# login_link.click()

user_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")
sleep(2)
user_input.send_keys("anonymousking09")
password_input.send_keys("anirudh0901")

login = browser.find_element_by_xpath("//button[@type='submit']")
login.click()

sleep(10)

browser.close()