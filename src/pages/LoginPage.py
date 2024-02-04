from selenium.common import NoSuchElementException

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # Web element locators
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.XPATH, "/html/body/div/div/div/div/div")
    ASAL_LOGO = (By.CSS_SELECTOR, "img[src*='Asal Technologies.svg']")
    AURORA_LOGO = (By.CSS_SELECTOR, "img[src*='Aurora.svg']")
    ORION_LOGO = (By.CSS_SELECTOR, "img[src*='Orion.svg']")

    def enter_username(self, username):
        self.type(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.type(self.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
        # Retrieve an error message element after a failed login attempt
        return self.find_element(self.ERROR_MESSAGE, timeout=10)

    def is_username_field_displayed(self):
        try:
            return self.find_element(self.USERNAME_FIELD).is_displayed()
        except NoSuchElementException:
            return False

    def is_password_field_displayed(self):
        try:
            return self.find_element(self.PASSWORD_FIELD).is_displayed()
        except NoSuchElementException:
            return False

    def is_sign_in_button_displayed(self):
        try:
            return self.find_element(self.LOGIN_BUTTON).is_displayed()
        except NoSuchElementException:
            return False

    def is_asal_logo_displayed(self):
        try:
            return self.find_element(self.ASAL_LOGO).is_displayed()
        except NoSuchElementException:
            return False

    def is_aurora_logo_displayed(self):
        try:
            return self.find_element(self.AURORA_LOGO).is_displayed()
        except NoSuchElementException:
            return False

    def is_orion_logo_displayed(self):
        try:
            return self.find_element(self.ORION_LOGO).is_displayed()
        except NoSuchElementException:
            return False