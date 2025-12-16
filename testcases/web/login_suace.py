from orbs.keyword.web import Web
def run():
    Web.open("https://www.saucedemo.com/")
    Web.set_text("id=user-name", "standard_user")
    Web.set_text("id=password", "secret_sauce")
    Web.take_screenshot("login_page.png")
    Web.click("id=login-button")
    Web.verify_text("class=app_logo", "Swag Labs")
    Web.take_screenshot("dashboard.png")

