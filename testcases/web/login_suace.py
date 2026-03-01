from orbs.keyword.web import Web, find_test_obj
from orbs.keyword.web import FailureHandling as FH

def run():
    Web.open("https://www.saucedemo.com/")
    Web.set_text(find_test_obj("object_repository\input_user-name.xml"), "standard_user")
    Web.set_text(find_test_obj("object_repository\input_password.xml"), "secret_sauce")
    Web.take_screenshot("login_page.png")
    Web.click(find_test_obj("object_repository\input_login-button.xml"))
    Web.verify_element_visible(find_test_obj("object_repository\div_swag_labs.xml"), 5)
    Web.take_screenshot("dashboard.png")
    Web.close()      

