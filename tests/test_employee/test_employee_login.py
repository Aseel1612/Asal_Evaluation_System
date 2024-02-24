from src.pages.HomePage import HomePage
import pytest


def verify_logos_displayed(login_page, device):
    assert login_page.is_asal_logo_displayed(), f"ASAL logo is not displayed on {device}"
    assert login_page.is_aurora_logo_displayed(), f"AURORA logo is not displayed on {device}"
    assert login_page.is_orion_logo_displayed(), f"ORION logo is not displayed on {device}"


@pytest.mark.parametrize("device", ["Mobile", "Tablet", "Desktop"])
def test_responsive_layout(login_page, config, screen_sizes, device):
    login_page.driver.set_window_size(screen_sizes[device]["width"], screen_sizes[device]["height"])
    assert login_page.is_at(), "The browser is not on the login page."
    verify_logos_displayed(login_page, device)
    login_page.driver.save_screenshot(f"screenshots/{device}_login_page.png")


def test_valid_login(login_page, config):
    assert login_page.is_at(), "The browser is not on the login page."
    login_page.login(
        config['employee']['valid_credentials']['username'],
        config['employee']['valid_credentials']['password']
    )
    home_page = HomePage(login_page.driver)
    assert home_page.is_at(), "The browser is not on the home page after login."


def test_invalid_login(login_page, config):
    assert login_page.is_at(), "The browser is not on the login page."
    login_page.login(config['employee']['invalid_credentials']['username'],
                     config['employee']['invalid_credentials']['password'])
    assert login_page.get_error_message(), "Error message should be displayed for invalid login."
