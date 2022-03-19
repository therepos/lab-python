from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# XPath selectors
NEW_CHAT_BTN = '/html/body/div[1]/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div/span'
INPUT_TXT_BOX = '/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]'
ONLINE_STATUS_LABEL = '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[2]/span'

# Replace below with the list of targets to be tracked
TARGETS = {'"Check"': '+65 1234 5678'}
log = ""

# Replace below path with the absolute path
browser = webdriver.Chrome(r'C:\Python\Scripts\chromedriver.exe')

# Load Whatsapp Web page
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)

while True:
    # Clear screen
    os.system('cls')

    # For each target
    for target in TARGETS:
        tryAgain = True

        # Wait untill new chat button is visible
        new_chat_title = wait.until(EC.presence_of_element_located((By.XPATH, NEW_CHAT_BTN)))

        while (tryAgain):
            try:
                # Click on new chat button
                new_chat_title.click()

                # Wait untill input text box is visible
                input_box = wait.until(EC.presence_of_element_located((By.XPATH, INPUT_TXT_BOX)))

                time.sleep(0.5)

                # Write phone number
                input_box.send_keys(TARGETS[target])

                time.sleep(1)

                # Press enter to confirm the phone number
                input_box.send_keys(Keys.ENTER)

                time.sleep(5)
                tryAgain = False

                try:
                    try:
                        browser.find_element_by_xpath(ONLINE_STATUS_LABEL)
                        log = target + ' is online'
                        print(target + ' is online')
                    except:
                        log = target + ' is offline'
                        print(target + ' is offline')
                    time.sleep(1)
                    with open("whatsapplog.csv","a") as f:
                        data = time.ctime(time.time()) + " " + log
                        print(data, file=f)
                except:
                    print('Exception 1')
                    time.sleep(10)
            except:
                print('Exception 2')
                time.sleep(4)


##  =============================
##  REFERENCES
##  =============================
##  https://www.macheronte.com/en/python-how-to-get-notified-when-someone-is-online-on-whatsapp/
##  https://www.macheronte.com/en/python-how-to-get-notified-when-someone-is-online-on-whatsapp_2/
##  https://www.geeksforgeeks.org/how-to-append-a-new-row-to-an-existing-csv-file/                
##
##  =============================
##  WIP
##  =============================
##  https://www.macheronte.com/en/python-send-sms-on-whatsapp-to-unsaved-numbers/
##  https://www.geeksforgeeks.org/share-whatsapp-web-without-scanning-qr-code-using-python/
