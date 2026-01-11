from behave import given, when, then
from orbs.mobile_factory import MobileFactory
import time
from appium.webdriver.common.appiumby import AppiumBy
from orbs.keyword.mobile import Mobile
from orbs.log import log

@given('the mobile app is installed on Sauce Labs device')
def step_app_installed(context):
    Mobile.launch("com.swaglabsmobileapp", "com.swaglabsmobileapp.MainActivity", True)
    time.sleep(10)  # Give app time to load
    Mobile.take_screenshot("app_launched.png")

@when('the user enters username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):    
    Mobile.set_text("accessibility_id=test-Username", username)
    Mobile.set_text("accessibility_id=test-Password", password)
    Mobile.take_screenshot("credentials_entered.png")

@when('the user taps the login button')
def step_tap_login(context):
    Mobile.click("accessibility_id=test-LOGIN")
    time.sleep(3)

@then('the home screen should be displayed')
def step_verify_home(context):
    try:
        Mobile.verify_element_visible("accessibility_id=test-PRODUCTS")
        assert True, "Home screen displayed"
        Mobile.take_screenshot("home_screen.png")
    except Exception as e:
        Mobile.take_screenshot("home_screen_error.png")
        log.error(f"Error verifying home screen: {str(e)}") 
        assert False, f"Home screen not displayed: {str(e)}"
    finally:
        # Mobile.quit()   
        Mobile.terminate_app("com.swaglabsmobileapp")
        Mobile.quit()