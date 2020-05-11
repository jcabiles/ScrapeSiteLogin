from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import yaml
import os
from datetime import datetime

config = yaml.safe_load(open('config.yml'))

# when ready, add lines to let selenium run w/o opening browser
# op = webdriver.ChromeOptions()
# op.add_argument('headless')

# instantiate webdriver and find login button
driver = webdriver.Chrome(#options=op
     )
driver.get(config['site'])
driver.find_element_by_xpath(
    '//*[@id="masthead"]/div/div/div/div/div[2]/ul/li/a[1]').click()

# enter credentials
driver.find_element_by_name("log").send_keys(config['username'])
driver.find_element_by_name("pwd").send_keys(config['password'])
driver.find_element_by_xpath(
    '//*[@id="login-modal"]/div/div/form/button').click()

# navigate dropdown
driver.find_element_by_xpath(
    '//*[@id="masthead"]/div/div/div/div[2]/ul/li[5]/button').click()
driver.find_element_by_xpath(
    '//*[@id="masthead"]/div/div/div/div[2]/ul/li[5]/ul/li[4]/a').click()

# click first entry and get title
driver.find_element_by_class_name("title-link").click()
post_title = driver.title
post_date = driver.find_element_by_class_name("time-ago").text
post_date = datetime.strptime(post_date, '%B %d, %Y')
post_date = post_date.strftime('%Y-%m-%d')
