from orbs.keyword.web import Web, find_test_obj
from orbs.keyword.web import FailureHandling as FH
from orbs.data import load_data, ddt


@ddt("login_sauce.csv", scenario="scenario", where=dict(scenario="valid"))
def run(data):
    # data = load_data("login_sauce.csv").where(scenario="valid").first()
    Web.open("https://www.saucedemo.com/")
    Web.set_text(find_test_obj("object_repository\input_user-name.xml"), data["name"])
    Web.set_text(find_test_obj("object_repository\input_password.xml"), data["password"])
    Web.take_screenshot("login_page.png")
    Web.click(find_test_obj("object_repository\input_login-button.xml"))
    # Web.verify_element_visible(find_test_obj("object_repository\div_swag_labs.xml"), 5)
    Web.verify_text_present(data['expected_result'])
    Web.take_screenshot("dashboard.png")
    Web.close()      

