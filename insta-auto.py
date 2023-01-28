
import ait
import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.instagram.com/")
driver.maximize_window
inp_xpath_search = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input"
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
input_box_search.send_keys("thedot_tech")
time.sleep(2)

inp_xpath_password = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input"
input_box_password = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_password))
input_box_password.click()
input_box_password.send_keys("thedotthedot")
time.sleep(2)

inp_xpath_login_btn = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button"
inp_xpath_login_btn = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_login_btn))
inp_xpath_login_btn.click()
time.sleep(3)

inp_xpath_new_btn_one = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button"
inp_xpath_new_btn_one = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_new_btn_one))
inp_xpath_new_btn_one.click()
time.sleep(2)


inp_xpath_new_btn_two = "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"
inp_xpath_new_btn_two = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_new_btn_two))
inp_xpath_new_btn_two.click()
time.sleep(2)



inp_xpath_new_btn_create_btn = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div"
inp_xpath_new_btn_create_btn = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_new_btn_create_btn))
inp_xpath_new_btn_create_btn.click()
time.sleep(2)


# inp_xpath_new_btn_upload_btn = "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button"
# inp_xpath_new_btn_upload_btn = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_new_btn_upload_btn))
# inp_xpath_new_btn_upload_btn.click()
# time.sleep(2)


time.sleep(2)
img_upload=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button').click()
time.sleep(2)
path = "F:\python-whatsapp-automation\pic.jpeg" # your imagepath
pyautogui.write(path) 
time.sleep(2)
pyautogui.press('enter')

time.sleep(1)
inp_xpat_image_next_btn = "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button"
inp_xpat_image_next_btn = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpat_image_next_btn))
inp_xpat_image_next_btn.click()
time.sleep(1)

inp_xpat_image_next_btn_one = "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button"
inp_xpat_image_next_btn_one = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpat_image_next_btn_one))
inp_xpat_image_next_btn_one.click()
time.sleep(2)

inp_xpat_caption_text = "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea"
inp_xpat_caption_text = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpat_caption_text))
inp_xpat_caption_text.send_keys("This post is posted by theDot Clan Bot")
time.sleep(0.5)


time.sleep(0.5)
inp_xpat_share_btn = "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button"
inp_xpat_share_btn = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpat_share_btn))
inp_xpat_share_btn.click()
time.sleep(0.5)

# Post Image Upload Done




