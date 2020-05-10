from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import yaml
import os

# instantiate webdriver and find login button
config = yaml.safe_load(open('config.yml'))
driver = webdriver.Chrome()
driver.get(config['site'])


