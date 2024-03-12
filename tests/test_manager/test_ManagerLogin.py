

def test_manager_login_with_valid_credentials_redirects_to_home_page(manager_login_page):
    home_page = manager_login_page.login_with_valid_credentials()
    assert home_page.check_page_title() == "ASAL Technologies – PERFORMANCE EVALUATION", \
        "The browser is not on the home page after login."


def test_manager_login_with_invalid_credentials_shows_error_message(manager_login_page):
    manager_login_page.login_with_invalid_credentials()
    assert manager_login_page.get_error_message(), "Error message should be displayed for invalid login."
