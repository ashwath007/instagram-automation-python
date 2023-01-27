from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def login():
    contact = "Rolex"
    text = "Hey, this message was sent using Selenium"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://web.whatsapp.com/")
    print("Scan QR Code, And then Enter")
    input()
    print("Logged In")
    inp_xpath_search = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]"
    print(inp_xpath_search)
    input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
    print(inp_xpath_search)
    input_box_search.click()
    time.sleep(2)
    input_box_search.send_keys(contact)
    time.sleep(2)
    selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
    selected_contact.click()
    inp_xpath = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    time.sleep(2)
    input_box.send_keys(text + Keys.ENTER)
    time.sleep(2)
    driver.quit()



def sendMsg():
    pass        



# Automation Flow
login()







