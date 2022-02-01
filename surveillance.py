import csv
import re
import itertools
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import webbrowser as web
import pyautogui as pg
from pathlib import Path

firefox_options = Options()
firefox_options.add_argument("--headless")

def runner():
    url = "https://www.homeq.se/search?rentMax=7000&is_everyone=true&selectedShapes=municipality.1480%3B4a59d4d634e77b804dd53f9a14964d540cacec0501c8c13dc737185f389ee45b%3BG%C3%B6teborg&selectedShapes=municipality.1402%3Bb55242e541450f57109d24cf042d4d2c5614310154e2649937bd66d65b4abb2e%3BPartille&selectedShapes=municipality.1481%3B6c53a0b0f33c87677c10d3bc23fe993f0701805d58482941d03238f71d07bd44%3BM%C3%B6lndal "
    browser = webdriver.Firefox(executable_path='/home/ekudgan/Downloads/Surveillance/geckodriver', options=firefox_options)
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
                    browser = webdriver.Firefox(executable_path='/home/ekudgan/Downloads/Surveillance/geckodriver', options=firefox_options)
                    browser.get(curr_url)
                    html = browser.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    rows = str(soup.findAll('div', attrs={'class': 'homeq-ad-dates'}))
                    dates = re.sub('<[^>]*>', '', rows)
                    move_in =  re.search('(?<=Inflytt: )(.*)', dates).groups()[0][:10]
                    publish_date = re.search('(?<=Publicering: )(.*)', dates).groups()[0][:10]
                    
                    rows = str(soup.findAll('div', attrs={'class': 'homeq-ad-numbers'}))
                    pricing = re.sub('<[^>]*>', '', rows)
                    rent=re.match("(.*?) ",pricing).group()[2:].strip()
                    room_no = re.search(r'•(.*?)rum', pricing).group(1).strip()
                    area = re.search(r', (.*?)m', pricing).group(1).strip()
                    floor = re.search(r'ning(.*?)]', pricing).group(1).strip()
                    
                    browser.quit()
                    time.sleep(2)
                    
                    list_new_homes.append([tag['href'], move_in, publish_date, rent, room_no, area, floor])
                    wf.writerow([tag['href'], move_in, publish_date, rent, room_no, area, floor])

    csv_file.close()
    time.sleep(5)
    # TODO - send message cleanly
    if len(list_new_homes) != 0:
        print("Sending new apartments")
        numbers = ["+46735799272","+919423990720"]
        for phone in numbers:
            for home in list_new_homes: 
                message = "https://web.whatsapp.com/send?phone=" + phone + "&text=" + home[0]
                web.open(message)            
                width, height = pg.size()            
                pg.click(width / 2, height / 2)
                time.sleep(10)
                pg.press('enter')
                time.sleep(10)
                pg.hotkey('ctrl', 'w')
                print("Sent")
    return


if __name__ == "__main__":
    while 1:
        runner()
        t = time.localtime()
        print("Slept at", time.strftime("%H:%M:%S", t))
        time.sleep(450)
        
