from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.XPATH, "/html/body/div/div/div/div/div")
    ASAL_LOGO = (By.CSS_SELECTOR, "img[src*='Asal Technologies.svg']")
    AURORA_LOGO = (By.CSS_SELECTOR, "img[src*='Aurora.svg']")
    ORION_LOGO = (By.CSS_SELECTOR, "img[src*='Orion.svg']")

    def login(self, username, password):
        self.type(self.USERNAME_FIELD, username)
        self.type(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        if self.is_element_visible(self.ERROR_MESSAGE, timeout=10):
            return self.find_element(self.ERROR_MESSAGE).text
        return None

    def is_username_field_displayed(self):
        return self.is_element_visible(self.USERNAME_FIELD)

    def is_password_field_displayed(self):
        return self.is_element_visible(self.PASSWORD_FIELD)

    def is_sign_in_button_displayed(self):
        return self.is_element_visible(self.LOGIN_BUTTON)

    def is_asal_logo_displayed(self):
        return self.is_element_visible(self.ASAL_LOGO)

    def is_aurora_logo_displayed(self):
        return self.is_element_visible(self.AURORA_LOGO)

    def is_orion_logo_displayed(self):
        return self.is_element_visible(self.ORION_LOGO)
