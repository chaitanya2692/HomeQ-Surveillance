import csv
import itertools
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import webbrowser as web
import pyautogui as pg
import pywhatkit
import os

chrome_options = Options()
chrome_options.add_argument("--headless")

def runner():
    url = "https://www.homeq.se/search?roomMin=2&areaMin=50&rentMax=10000&sorting=publish_date.desc&is_everyone=true&is_student=true&selectedShapes=urban_area.4368%3B5e076ebbc599fa845a722a9a378eb5e2742628a8317c7703145432ae2f78477c%3BG%C3%B6teborg"
    browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
    browser.get(url)
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    browser.quit()
    list_homes = []
    list_new_homes = []
    filename = 'all_homes.csv'

    f = open(filename, 'a+', encoding="utf-8")
    f.close()

    with open(filename, 'r', encoding="utf-8") as csv_file:
        rf = csv.reader(csv_file)
        list_homes = list(itertools.chain(*rf))
    csv_file.close()

    with open(filename, 'a+', newline='', encoding="utf-8") as csv_file:
        wf = csv.writer(csv_file)
        for tag in soup.find_all('a', href=True):
            if "https://www.homeq.se/lagenhet/" in tag['href']:
                curr_url = str(tag['href'])
                if curr_url not in list_homes:
                    print(curr_url)
                    list_new_homes.append([curr_url])
                    wf.writerow([curr_url])

    csv_file.close()
    time.sleep(1)

    if len(list_new_homes) != 0:
        print("Sending new apartments")
        numbers = ["+46735799272", "+46760714945", "+919423990720"]
        for phone in numbers:
            for home in list_new_homes: 
                pywhatkit.sendwhatmsg_instantly(phone, home[0], 90, True, 5)
                time.sleep(1)
    return


if __name__ == "__main__":
    runner()
    t = time.localtime()
    print("Slept at", time.strftime("%H:%M:%S", t))   
