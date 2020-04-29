import requests
from bs4 import BeautifulSoup
import yaml

# set up session login
config = yaml.safe_load(open('config.yml'))
session = requests.Session()
payload = {'_username': config['username'],
           '_password': config['password']
           }
s = session.post(config['site'], data=payload)

# test
site = config['site']
test = session.get(f'{site}/circles/mindfulness')

