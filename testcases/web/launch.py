from orbs.runner import Runner
from orbs.browser_factory import BrowserFactory
from orbs.keyword.web import Web 

def run():
    # without abstration
    # browser_factory = BrowserFactory()
    # driver = browser_factory.create_driver()
    # driver.get("https://katalon-demo-cura.herokuapp.com/")

    # with abstration
    Web.open("https://katalon-demo-cura.herokuapp.com/")
    