# -*- coding: utf-8 -*-
'''
Firts lines of code
'''

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
import requests

group_id = 'INSERT GROUP IP'
username = 'INSERT YOUR USERNAME'
password = 'INSERT YOUR PASSWORD'

browser = webdriver.Firefox()
browser.set_window_size(1024, 768)

browser.get('https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2Fgroups%2F' + group_id)
element_email = browser.find_element_by_id('email')
element_email.send_keys(username)
element_password = browser.find_element_by_id('pass')
element_password.send_keys(password)
element_password.send_keys(Keys.RETURN)

wait_result = WebDriverWait(browser, 20).until(
    condition.presence_of_element_located((By.ID, "group_mall_" + group_id))
)

if wait_result:
    source_code = browser.page_source
    group_mall = browser.find_element_by_id('group_mall_' + group_id)
    feed = group_mall.text

    # print(group_mall)
    # print(dir(group_mall))
    
    elements = group_mall
    
    print(feed)

