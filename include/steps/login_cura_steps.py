from orbs.keyword.web import Web

@given('the user opens the login page')
def step_open_login(context):
    Web.open("https://katalon-demo-cura.herokuapp.com/")
    Web.maximize_window()


@when('the user fill username {username} and password {password}')
def step_username(context, username, password):
    Web.wait_for_visible("id=btn-make-appointment", 10)
    Web.click("id=btn-make-appointment")
    Web.set_text("id=txt-username", username)
    Web.set_text("id=txt-password", password)
    Web.click("id=btn-login")


@then('the user should see the dashboard')
def step_dashboard(context):
    Web.wait_for_visible("id=menu-toggle", 10)
    Web.take_screenshot("login_success.png")