import time
from selenium.webdriver.chrome.options import Options
from behave import given, when, then
from selenium import webdriver

from orbs.browser_factory import BrowserFactory
from orbs.mobile_factory import MobileFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user opens the login page')
def step_open_login(context):
    browser_factory = BrowserFactory()
    context.driver = browser_factory.create_driver()
    context.driver.get("https://katalon-demo-cura.herokuapp.com/")
    context.driver.maximize_window()

@when('the user fill username {username} and password {password}')
def step_username(context, username, password):
    # wait for the page to load
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(("id", "btn-make-appointment"))
    )
    context.driver.find_element("id", "btn-make-appointment").click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(("id", "txt-username"))
    )
    context.driver.find_element("id", "txt-username").send_keys(username)
    context.driver.find_element("id", "txt-password").send_keys(password)
    context.driver.find_element("id", "btn-login").click()

@then('the user should see the dashboard')
def step_dashboard(context):
    context.driver.save_screenshot("dashboard.png")