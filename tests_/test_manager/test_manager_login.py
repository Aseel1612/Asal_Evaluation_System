import time

import pytest

from src.pages.HomePage import HomePage
from src.pages.LoginPage import LoginPage


@pytest.fixture(scope='module')
def login_page(manager_browser, config):
    # Initialize LoginPage with the browser instance provided by the 'manager_browser' fixture
    return LoginPage(manager_browser)


@pytest.mark.order(1)
def test_invalid_login(manager_browser, config, login_page):
    # Navigate to the login page using the 'baseUrl' from the base configuration
    manager_browser.get(config['baseUrl'])

    # Perform an invalid login using credentials from the manager configuration
    login_page.login(
        config['manager']['invalid_manager_credentials']['username'],
        config['manager']['invalid_manager_credentials']['password']
    )

    error_message = login_page.get_error_message()

    assert error_message, "Error message should be displayed for invalid login."


@pytest.mark.order(2)
def test_valid_login(manager_browser, config, login_page):
    # Navigate to the login page using the 'baseUrl' from the base configuration
    manager_browser.get(config['baseUrl'])

    # Perform a valid login using credentials from the manager configuration
    login_page.login(
        config['manager']['valid_manager_credentials']['username'],
        config['manager']['valid_manager_credentials']['password']
    )
    home_page = HomePage(manager_browser)

    # Alternatively, if you do not have WebDriverWait set up, a simple assertion could be:
    # This assumes you have a method in your LoginPage to check for the "My Team" element
    assert home_page.is_my_team_visible(), "My Team link should be visible for managers"
