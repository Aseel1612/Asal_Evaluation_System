import pytest


@pytest.mark.parametrize("device", ["Mobile", "Tablet", "Desktop"])
def test_responsive_layout(employee_login_page, screen_sizes, device):
    employee_login_page.set_window_size(screen_sizes[device]["width"], screen_sizes[device]["height"])
    logos = ["is_asal_logo_displayed", "is_aurora_logo_displayed", "is_orion_logo_displayed"]
    assert all(getattr(employee_login_page, logo)() for logo in logos), \
        f"One or more logos are not displayed on {device}"


def test_employee_login_with_valid_credentials_redirects_to_home_page(employee_login_page):
    home_page = employee_login_page.login_with_valid_credentials()
    assert home_page.check_page_title() == "ASAL Technologies – PERFORMANCE EVALUATION", \
        "The browser is not on the home page after login."


def test_employee_login_with_invalid_credentials_shows_error_message(employee_login_page):
    employee_login_page.login_with_invalid_credentials()
    assert employee_login_page.get_error_message(), "Error message should be displayed for invalid login."
