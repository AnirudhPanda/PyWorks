from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

three = 3
twentyfive = 25
one = 1

chrome_path = r"C:\Users\HP\AppData\Local\Programs\Python\Python38-32/chromedriver.exe"

driver = webdriver.Chrome(chrome_path)

URL = "https://web.whatsapp.com/"
driver.get(URL)

time.sleep(twentyfive)

def send_messages():

    chats = int(input("Enter the number of personal chats/groups you would want to message "))

    for chat in range(chats):

        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div').click()

        name = input("Enter name whom u want to message ")
        time.sleep(three)

        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]').send_keys(name)

        time.sleep(three)

        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)

        done = one
        while done:
            message = input("Enter the message you want to enter ")
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(message)
            time.sleep(three)

            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button').click()

            print("Would you want to send another message to the same contact ?")
        
            done = int(input("Enter 1 to continue, 0 to stop "))
        
    print("All messages sent successfully")

send_messages()

