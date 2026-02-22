#!/usr/bin/env python3
"""
Generated test case: test_recorded_scenario
Created by Orbs Recorder on 2026-02-21 17:40:04
"""

from orbs.keyword.web import Web


def run():
    """Generated test case for test_recorded_scenario"""

    # Setup
    Web.open("https://www.saucedemo.com/")

    # Recorded interactions
    Web.click("id=user-name")
    Web.set_text("id=user-name", "standard_user")
    # Tab to next field
    Web.set_text("id=user-name", "standard_user")
    Web.set_text("id=password", "your_password_here")  # TODO: Replace with actual password
    Web.set_text("id=password", "secret_sauce")
    Web.click("id=login-button")
    # Navigation: https://www.saucedemo.com/inventory.html
    Web.click("xpath=//body/div/div/div/div[1]/div[2]/span")

    # Cleanup
    Web.close()