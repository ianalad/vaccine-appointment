#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 15:14:04 2021

@author: iana
"""

import os
import telegram

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException

from dotenv import load_dotenv


load_dotenv() # This loads the environmental variables from the .env file in the root folder

TELEGRAM_BOT_ID = ''
#TELEGRAM_SUPERGROUP_ID must be numerical
TELEGRAM_SUPERGROUP_ID = 
URL = 'https://siunsote.eaika.fi/koronarokote'

options = Options()
options.headless = True
d = webdriver.Firefox()
d.get(URL)

# Part that needs to be scraped
elem = d.find_element_by_class_name('row').click()
elem = d.find_element_by_class_name('col-md-12').click()
elem = d.find_element_by_id('channel_13_119').click()

def send(telegram_data, TELEGRAM_CHAT_ID, TELEGRAM_BOT_ID):
    """
    TELEGRAM_CHAT_ID must be a number!
    """
    bot = telegram.Bot(token=TELEGRAM_BOT_ID)
    bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=telegram_data)

def check_exists_by_xpath(xpath):
    try:
        d.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

xpath_list = ['//*[@id="channel_13_206"]/span', '//*[@id="channel_13_190"]/span']
location = ['Siilainen, Joensuu', 'Rääkkylä']

for i in range(len(xpath_list)):
    try:
        if i == 1:
            elem = d.find_element(By.XPATH, '//*[@id="landing_vaccination"]/div/div[1]/button[1]').click()
            elem = d.find_element_by_id('channel_13_114').click()
                
        elem = check_exists_by_xpath(xpath_list[i])
        
        if elem == False:
            
            telegram_data = "Moi! Vaccination time is available in " + location[i] + "." + " Check out: https://siunsote.eaika.fi/koronarokote"
            send(telegram_data, TELEGRAM_SUPERGROUP_ID, TELEGRAM_BOT_ID)
            print("Time is available in " + location[i])
            d.close() #Close the connection in a browser
            
            if i == 0:
                break
            
        else:
            if i == 1:
                d.close() #Close the connection in a browser
            print("No time is available in " + location[i])
            
    except WebDriverException:
        d.close() #Close the connection in a browser
        print("Error detected")