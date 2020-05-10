from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import yaml
import os

# instantiate webdriver and find login button
config = yaml.safe_load(open('config.yml'))
driver = webdriver.Chrome()
driver.get(config['site'])
driver.find_element_by_name("modal-button").click()

# enter credentials
driver.find_element_by_id("log").send_keys(config['username'])
driver.find_element_by_id("pwd").send_keys(config['password'])
driver.find_element_by_name("log in").click()