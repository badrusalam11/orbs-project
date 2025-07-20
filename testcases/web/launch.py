from orbs.runner import Runner
from orbs.browser_factory import BrowserFactory

def run():
    browser_factory = BrowserFactory()
    driver = browser_factory.create_driver()
    driver.get("https://katalon-demo-cura.herokuapp.com/")