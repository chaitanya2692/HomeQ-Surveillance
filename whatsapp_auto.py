

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time, os
import webbrowser as web
from pynput.keyboard import Key, Controller


for i in range(5):
    
    # options = Options()
    # fp = webdriver.FirefoxProfile("kaliprofile")
    # # useragent = "Mozilla/5.0 (X11; Linux i686; rv:77.0) Gecko/20100101 Firefox/77.0" #works perfectly fine without useragent modification in windows awa heroku
    # # fp.set_preference("general.useragent.override", useragent)
    # options.add_argument('--no-sandbox')
    # options.add_argument("--headless")
    # # driver = webdriver.Firefox(firefox_profile=fp, options=options)
    # driver = webdriver.Firefox(firefox_profile=fp, options=options, executable_path=os.environ.get("GECKODRIVER_PATH"),firefox_binary=os.environ.get("FIREFOX_BIN"))
    
    message = "https://web.whatsapp.com/send?phone=" + "46735799272" + "&text=hello_" + str(i)
    # whatsapp_browser = webdriver.Firefox(executable_path='/home/ekudgan/Downloads/Surveillance/geckodriver', options=firefox_options)
    # whatsapp_browser.get(message)
    # if i == 0:
    #     time.sleep(15)
    # whatsapp_browser.find_elements_by_class_name('_4sWnG')[0].click()
    # time.sleep(5)
    # whatsapp_browser.quit()
    
    web.open(message)
    time.sleep(5)
    
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)    
    time.sleep(5)
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
    print("Sent")
