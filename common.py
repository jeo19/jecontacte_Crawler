# -*- coding: ISO-8859-1 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests
import math
import urllib.request
import csv
import re

product_count = 0
# options = webdriver.ChromeOptions()
# options.add_argument("headless")
# options.add_argument("window-size=1920x1080")
# options.add_argument("--disable-gpu")
path = "chromedriver"
driver = webdriver.Chrome(path)
all_userInfo = []


def openSite(startUrl):
    try:
        driver.get(startUrl)
        # driver.implicitly_wait(3)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, "standardblock")))
        # driver.get_screenshot_as_file("jecontacte.png")
        # Wait untill ID "standardblock".
        return driver
    except:
        driver.get(startUrl)
        wait = WebDriverWait(driver, 10)
        # driver.implicitly_wait(3)
        return driver


def select_attr(gender, fromAge, toAge, country, region):
    try:
        sel_gender = driver.find_element_by_css_selector(gender)
        sel_gender.click()
        sel_fromAge = driver.find_element_by_css_selector(fromAge)
        sel_fromAge.click()
        sel_toAge = driver.find_element_by_css_selector(toAge)
        sel_toAge.click()
        sel_country = driver.find_element_by_css_selector(country)
        sel_country.click()
        sel_region = driver.find_element_by_css_selector(region)
        sel_region.click()
    except Exception as e:
        print(type(e))


def countPage():
    try:
        page = 1
        currentUrl = driver.current_url
        global all_userInfo

        while 1:
            if page == 67:
                break
            driver.get(currentUrl + "&page=" + str(page))
            response = requests.get(driver.current_url)
            source = response.text
            # print(source)
            soup = BeautifulSoup(source, "html.parser")
            profile = soup.select("#pagecontainer > div > center > div > div > span ")
            summary = soup.select(
                "#pagecontainer > div > center > div.vignette_infos > div.wideDiv"
            )
            for profile_content, summary in zip(profile, summary):
                userInfo = []
                a, b = profile_content.text.split("\n")
                a = a.split()
                id = a[0].replace(",", "")
                age = a[1]
                c = re.findall("\d\sphotos", str(b))
                c = "".join(map(str, c))
                region = b.replace(c, "")
                userInfo.append(id)
                userInfo.append(age)
                userInfo.append(region)
                userInfo.append(summary.text)
                all_userInfo.append(userInfo)
            print("Total " + str(page) + "pages " + "was crawler!")
            page = page + 1
        return all_userInfo

    except Exception as e:
        print(e)


def saveResult(all_userInfo):
    global product_count
    f = open("male_young(18~24).csv", "a", encoding="ISO-8859-1", newline="")
    for userInfo in all_userInfo:
        id = userInfo[0]
        age = userInfo[1]
        region = userInfo[2].replace("\n", "").replace("\r", "")
        description = userInfo[3].replace("\n", "").replace("\r", "")
        wr = csv.writer(f)
        wr.writerow([id, age, region, description])
    f.close()
