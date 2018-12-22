# -*- coding: utf-8 -*-
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
path = "chromedriver"
driver = webdriver.Chrome(path)


def openSite(startUrl):
    try:
        driver.get(startUrl)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, "standardblock")))
        # Wait untill ID "standardblock".
    except:
        driver.get(startUrl)
        wait = WebDriverWait(driver, 10)
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
        count_select = driver.find_element_by_css_selector(
            "body > div.wrapper > div > div.main-container.col1-layout > div > div.col-main > div.page-title.category-title > p:nth-child(2)"
        )
        total_count = count_select.text.split(" ")
        totalPD = total_count[
            -1
        ]  # It will fetch the last item 298 of string "Your selection 1-24 items of 298"
        print(totalPD)
        totalPN = math.ceil(int(totalPD) / 24.0)  # 298 items divide 24 products
        print("Success:< countPage > function did execute!.........")
        return totalPN
    except:
        totalPD = total_count[
            -2
        ]  # It will fetch the last item 298 of string "Your selection 1-24 items of 298"
        print(totalPD)
        totalPN = math.ceil(int(totalPD) / 24.0)  # 298 items divide 24 products
        print("Success:< countPage > function did execute!.........")
        return totalPN


def hasImg_products():
    URL = driver.current_url
    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")
        products_tag = driver.find_elements_by_css_selector(
            "body > div.wrapper > div > div.main-container.col1-layout > div > div.col-main > div.category-products > ul > li > div.product-info > h2 > a"
        )  # fetching products
        hasImg_tag = soup.select(
            'img[id*="product-collection-image"]'
        )  # fetching img tags
        remove_tag = soup.select('img[data-src*="-51f.jpg"]')  # fetching non image tags
        products_name = []
        detail_url = []
        for index in remove_tag:
            hasImg_tag.remove(index)  # remove non img tags
        for hasImg in hasImg_tag:
            product = BeautifulSoup(str(hasImg), "html.parser")
            products_name.append(
                product.find("img")["alt"]
            )  # fetching products name having img
        for index in products_name:
            detail_url.append(
                soup.find("a", {"title": index})["href"]
            )  # fetching the url list of products having img

        print("Success:< hasImg_products > function was execute!.........")
        return detail_url
    except:
        print("Error: < hasImg_products > function is crashed!.........")


def get_Pinfo(URL_LIST):
    print(requests.get(URL_LIST))

    for product_url in URL_LIST:
        try:
            r = requests.get(product_url, timeout=27)
            soup = BeautifulSoup(r.text, "html.parser")
            product_name = soup.select(
                "body > div.wrapper > div > div.main-container.col1-layout > div > div.col-main > div.product-name.page-title > h1"
            )
            sku = soup.select(
                "#product_addtocart_form > div.product-main > div.product-info-bar > span.product-sku"
            )
            product_description = soup.select(
                "#product_addtocart_form > div.product-main > div.product-essential > div.product-tabs > div > div.tab-switcher.product-description > div"
            )
            if len(product_description) == 0:  # if product_description is none
                continue
            #     product_description=soup.select("#product_addtocart_form > div.product-main > div.product-essential > div.product-tabs > div > div.tab-switcher.product-description > div")
            #     product_description=soup.select("#product_addtocart_form > div.product-main > div.product-essential > div.product-tabs > div > div.tab-switcher.product-description > div
            product_img = soup.find("img", {"id": "image-main"})["href"]
            # get info
            product_name = product_name[0].text
            sku = sku[0].text
            product_description = product_description[0].text
            # save info
            saveResult(product_name, sku, product_description, product_img)
        except Exception as e:
            # # print(type(e))
            # print(e.args)
            print(e)
            print("Error: < get_Pinfo > function is crashed!.........")


def saveResult(product_name, sku, product_description, product_img):
    global product_count
    img_name = product_img.split("/")
    product_count = product_count + 1
    print(product_name)
    print(str(product_count) + " products is crawled!")
    sku = sku.replace("\n", "").replace("\r", "")
    product_name = product_name.replace("\n", "").replace("\r", "")
    product_description = product_description.replace("\n", "").replace("\r", "")
    f = open("product_details.csv", "a", encoding="utf-8", newline="")
    wr = csv.writer(f)
    wr.writerow([sku, product_name, product_description, img_name[-1]])
    f.close()
    urllib.request.urlretrieve(product_img, "./image/" + img_name[-1])

