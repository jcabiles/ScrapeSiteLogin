import mechanicalsoup
import yaml

config = yaml.safe_load(open('config.yml'))
browser = mechanicalsoup.StatefulBrowser()
browser.open(config['site'])

"""
Get login form to enter login and password.

Note that you'll need to need to open up your browser's dev tools
in order to find what username_login and password fields are called.
"""
form = browser.select_form()
form.set_input({"log": config['username'],
                "pwd": config['password']})
