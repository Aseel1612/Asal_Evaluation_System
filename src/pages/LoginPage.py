from src.pages.BasePage import BasePage
from src.pages.HomePage import HomePage


class LoginPage(BasePage):
    PAGE_NAME = "LoginPage"

    def __init__(self, driver, valid_credentials, invalid_credentials):
        super().__init__(driver)
        self.valid_credentials = valid_credentials
        self.invalid_credentials = invalid_credentials

    def login_with_valid_credentials(self):
        self.login(
            self.valid_credentials['username'],
            self.valid_credentials['password']
        )
        return HomePage(self.driver)

    def login_with_invalid_credentials(self):
        self.login(
            self.invalid_credentials['username'],
            self.invalid_credentials['password']
        )

    def login(self, username, password):
        self.type(self.PAGE_NAME, "USERNAME_FIELD", username)
        self.type(self.PAGE_NAME, "PASSWORD_FIELD", password)
        self.click(self.PAGE_NAME, "LOGIN_BUTTON")

    def get_error_message(self):
        if self.is_element_visible(self.PAGE_NAME, "ERROR_MESSAGE", timeout=10):
            return self.find_element(self.PAGE_NAME, "ERROR_MESSAGE").text
        return None

    def is_username_field_displayed(self):
        return self.is_element_visible(self.PAGE_NAME, "USERNAME_FIELD")

    def is_password_field_displayed(self):
        return self.is_element_visible(self.PAGE_NAME, "PASSWORD_FIELD")

    def is_sign_in_button_displayed(self):
        return self.is_element_visible(self.PAGE_NAME, "LOGIN_BUTTON")

    def is_asal_logo_displayed(self):
        return self.is_element_visible(self.PAGE_NAME, "ASAL_LOGO")

    def is_aurora_logo_displayed(self):
        return self.is_element_visible(self.PAGE_NAME, "AURORA_LOGO")

    def is_orion_logo_displayed(self):
        return self.is_element_visible(self.PAGE_NAME, "ORION_LOGO")

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)
