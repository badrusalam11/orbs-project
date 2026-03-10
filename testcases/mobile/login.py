# Test case: login

from orbs.keyword.mobile import Mobile
from orbs.config import config
import time


def run():
    Mobile.launch("com.swaglabsmobileapp", "com.swaglabsmobileapp.MainActivity", True)
    time.sleep(10)  # Give app time to load
    Mobile.take_screenshot("app_launched.png")

    Mobile.set_text("accessibility_id=test-Username", "standard_user")
    Mobile.set_text("accessibility_id=test-Password", "secret_sauce")
    Mobile.take_screenshot("credentials_entered.png")

    Mobile.click("accessibility_id=test-LOGIN")
    time.sleep(3)

    try:
        Mobile.verify_element_visible("accessibility_id=test-PRODUCTS")
        assert True, "Home screen displayed"
        Mobile.take_screenshot("home_screen.png")
    except Exception as e:
        Mobile.take_screenshot("home_screen_error.png")
        assert False, f"Home screen not displayed: {str(e)}"
    finally:
        # Mobile.quit()   
        Mobile.terminate_app("com.swaglabsmobileapp")
        Mobile.quit()