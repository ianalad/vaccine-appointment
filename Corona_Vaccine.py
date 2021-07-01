#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 15:14:04 2021

@author: iana
"""

import os
import datetime
import telegram

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException


TELEGRAM_BOT_ID = ''
# TELEGRAM_SUPERGROUP_ID must be a number
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

try:
    elem = d.find_element(By.XPATH, '//*[@id="channel_13_206"]/span')
    
    if elem.text != "EI VAPAITA AIKOJA" and elem.text != "Ei vapaita aikoja":
    
        telegram_data = "Moi! Vaccination time is available. Check out: https://siunsote.eaika.fi/koronarokote"
        
        def send(telegram_data, TELEGRAM_CHAT_ID, TELEGRAM_BOT_ID):
            """
            TELEGRAM_CHAT_ID must be a number!
            """
            bot = telegram.Bot(token=TELEGRAM_BOT_ID)
            bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=telegram_data)
        
        send(telegram_data, TELEGRAM_SUPERGROUP_ID, TELEGRAM_BOT_ID)
        print("Time has been sent")
        d.close() #Close the connection in a browser
    else:
        d.close() #Close the connection in a browser
        print("No time is available")
except WebDriverException:
    d.close() #Close the connection in a browser
    print("Error detected")
    

    
    
    
    
    
    
    
    

