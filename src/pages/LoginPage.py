from src.pages.BasePage import BasePage


class LoginPage(BasePage):
    PAGE_NAME = "LoginPage"

    def is_at(self):
        # Check if the browser is currently displaying the login page
        return self.is_element_visible(self.PAGE_NAME, "LOGIN_BUTTON")

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
