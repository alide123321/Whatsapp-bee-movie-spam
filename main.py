from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys


f = open("bee movie script.txt", "r")

browser = webdriver.Chrome()  # starts the chromedriver.exe
browser.get(('https://web.whatsapp.com/'))  # sets link and opens chrome

time.sleep(15)

try:
    textbox = browser.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')  # finds text bot
except:
    print("Could'nt find the text box please scan the QR code and click on the user you want to spam")
    browser.get(
        ('https://github.com/alide123321/Whatsapp-bee-movie-spam/blob/main/README.md'))
    sys.exit()


for x in f:
    textbox.send_keys(x + "\n")

textbox.send_keys("Sry bud")
