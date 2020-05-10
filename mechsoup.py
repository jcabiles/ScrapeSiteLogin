import mechanicalsoup
import yaml

config = yaml.safe_load(open('config.yml'))
browser = mechanicalsoup.StatefulBrowser()
browser.open(config['site'])

form = browser.select_form()
form.set_input({"log": config['username'],
                "pwd": config['password']})
