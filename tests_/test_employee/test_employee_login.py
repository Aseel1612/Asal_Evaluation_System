from src.pages.LoginPage import LoginPage

import pytest


@pytest.fixture(scope='module')
def login_page(employee_browser, config):
    return LoginPage(employee_browser)


def verify_logos_displayed(login_page, device):
    assert login_page.is_asal_logo_displayed(), f"ASAL logo is not displayed on {device}"
    assert login_page.is_aurora_logo_displayed(), f"AURORA logo is not displayed on {device}"
    assert login_page.is_orion_logo_displayed(), f"ORION logo is not displayed on {device}"


@pytest.mark.order(2)
@pytest.mark.parametrize("device", ["Mobile", "Tablet", "Desktop"])
def test_responsive_layout(employee_browser, config, screen_sizes, login_page, device):
    width = screen_sizes[device]["width"]
    height = screen_sizes[device]["height"]
    employee_browser.set_window_size(width, height)
    employee_browser.get(config['baseUrl'])
    assert login_page.is_username_field_displayed(), f"Username field not displayed on {device}"
    assert login_page.is_password_field_displayed(), f"Password field not displayed on {device}"
    assert login_page.is_sign_in_button_displayed(), f"Sign-in button not displayed on {device}"
    verify_logos_displayed(login_page, device)
    employee_browser.save_screenshot(f"screenshots/{device}_login_page.png")


@pytest.mark.order(3)
def test_invalid_login(employee_browser, config, login_page):
    employee_browser.get(config['baseUrl'])
    login_page.login(
        config['employee']['invalid_credentials']['username'],
        config['employee']['invalid_credentials']['password']
    )

    error_message = login_page.get_error_message()
    assert error_message, "Error message should be displayed for invalid login."


@pytest.mark.order(4)
def test_valid_login(employee_browser, config, login_page):
    employee_browser.get(config['baseUrl'])

    login_page.login(
        config['employee']['valid_credentials']['username'],
        config['employee']['valid_credentials']['password']
    )

    assert "Employee" in employee_browser.current_url, \
        f"URL should contain 'Employee' after valid login, but was {employee_browser.current_url}."
