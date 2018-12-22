# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests
from common import openSite, select_attr, countPage, hasImg_products, get_Pinfo
import math
from multiprocessing import Pool

maxium = 0
page = 1
path = "chromedriver"
# file=open("urlList.txt","r")
with open("urlList.txt") as START_URL:
    for goURL in START_URL:
        driver = openSite(goURL)  # Open the site
        gender = "#menulinks > form > select:nth-child(5) > option:nth-child(2)"
        fromAge = "#menulinks > form > select:nth-child(8) > option:nth-child(1)"
        toAge = "#menulinks > form > select:nth-child(9) > option:nth-child(7)"
        country = "#menupaysdropdown > option:nth-child(3)"
        region = "#menulinks > form > input[type='submit']:nth-child(18)"
        select_attr(gender, fromAge, toAge, country, region)
        exit()
        totalPN = countPage()  # fetch total page number
        current_url = driver.current_url
        for page in range(1, totalPN + 1):
            driver.get(current_url + "?p=" + str(page))
            time.sleep(8)
            hasImg_urlList = hasImg_products()  # Get URL list of products having img
            get_Pinfo(hasImg_urlList)
