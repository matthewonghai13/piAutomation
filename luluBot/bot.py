import pyperclip
import requests
import random
import string
import time
import timeit
import sys
import re
from threading import Thread
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from faker import Faker
from random import randrange
from termcolor import colored
from sys import platform

def main():
    chrome_options = Options()
    print(platform)
    # TODO: fix not working in headless
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=chrome_options)
    driver.get("https://shop.lululemon.com/p/men-shorts/Pace-Breaker-Short-5-Lined/_/prod10080318?color=0001&sz=XS")
    # driver.get("https://shop.lululemon.com/p/men-shorts/Pace-Breaker-Short-5-Lined/_/prod10080318?color=0001&sz=M")
    sleep(10)
    if len(driver.find_elements_by_id("purchase-attributes-size-notification-error")) > 0:
        print("Nothing Found.")
    else:
        print("In stock!")
    driver.close()


if __name__ == '__main__':
    main()