#!/usr/local/bin/python3
""" Take care of common functions to get data from screener.in
"""
import json, time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

config = 'config.json'
conf = json.load(open(config))

def get_instance(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=options)
    return driver

def login(driver, credentials):
    driver.get("https://www.screener.in/login/")
    u = driver.find_element_by_id("id_username")
    p = driver.find_element_by_id("id_password")
    username = credentials['username']
    password = credentials['password']
    btn = driver.find_element_by_class_name("btn")
    u.send_keys(username)
    p.send_keys(password)
    btn.submit()
    if driver.current_url == 'https://www.screener.in/dash/':
        return (True, driver)
    else:
        return(False, driver)

def get_url(driver):
    time.sleep(5)
    driver.get(url)

def cleanup(driver):
    driver.quit()
