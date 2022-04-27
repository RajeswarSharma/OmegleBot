import selenium
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from plyer import notification
import msvcrt as m


def notify():
    notification.notify(
        title='Bot requires Attention',
        message='Bot stuck',
        app_icon=None,
        timeout=60,
    )



driver = webdriver.Chrome(
    r'C:\\Users\\Rajeswar Sharma\\Documents\\python\\chromedriver_win32\\chromedriver')
driver.get("https://www.omegle.com/")

Xpath_text_button = '//img[@id="textbtn"]'
Xpath_new_connect = '//button[@class="disconnectbtn"]'
Xpath_new_message = '//textarea[@class="chatmsg"]'
Xpath_sent_btn = '//button[@class="sendbtn"]'
tags_class_name = '//input[@class="newtopicinput" and @type="text"]'

msg = "CUSTOM message"
driver.get("https://www.omegle.com/")
tags_object = driver.find_elements_by_xpath(tags_class_name)
tags_object[0].send_keys("indian\nindia\ndesi\ndelhi\n")
time.sleep(2)
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)

text_mode_button = driver.find_element_by_xpath(Xpath_text_button)
text_mode_button.click()

counter = 0
fail = 0

print("Elements detected")
while True:
    try:
        time.sleep(2)
        new_connect_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(
            expected_conditions.presence_of_element_located((By.XPATH, Xpath_new_connect)))
        sent_btn = driver.find_element_by_xpath(Xpath_sent_btn)
        if driver.find_element_by_class_name('chatmsg') == 0:
            print("chatmsg not found")
            new_connect_button.click()
            print("Clicked on new connection")
        else:

            new_message = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, "chatmsg")))
            time.sleep(3)
            new_message.send_keys(msg)
            sent_btn.click()
            time.sleep(2)
            new_connect_button.click()
            new_connect_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(
                expected_conditions.presence_of_element_located((By.XPATH, Xpath_new_connect)))
            time.sleep(1)
            new_connect_button.click()
            counter += 1
            fail = 0
            print(counter)
            new_connect_button.click()
    except:
        fail += 1
        if fail >= 20:
            notify()
            fail = 0
        new_connect_button.click()

    finally:
        continue
