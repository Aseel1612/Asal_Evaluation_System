import pytest

from src.pages.HomePage import HomePage
from src.pages.LoginPage import LoginPage


@pytest.fixture(scope='module')
def login_page(manager_browser, config):
    return LoginPage(manager_browser)


@pytest.mark.order(1)
def test_invalid_login(manager_browser, config, login_page):
    manager_browser.get(config['baseUrl'])

    login_page.login(
        config['manager']['invalid_manager_credentials']['username'],
        config['manager']['invalid_manager_credentials']['password']
    )

    error_message = login_page.get_error_message()

    assert error_message, "Error message should be displayed for invalid login."


@pytest.mark.order(2)
def test_valid_login(manager_browser, config, login_page):
    manager_browser.get(config['baseUrl'])

    login_page.login(
        config['manager']['valid_manager_credentials']['username'],
        config['manager']['valid_manager_credentials']['password']
    )
    home_page = HomePage(manager_browser)

    assert home_page.check_page_title(), "The page tite is not checked"
