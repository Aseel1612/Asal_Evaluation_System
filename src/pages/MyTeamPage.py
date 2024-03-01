from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from src.pages.BasePage import BasePage


class MyTeamPage(BasePage):
    PAGE_NAME = "MyTeamPage"

    def __init__(self, driver):
        super().__init__(driver)

    def open_employee_evaluation(self, employee_name):
        my_team_menu_item_locator = ("xpath", "//a[@href='/Supervisor/getEmployees']")
        self.wait_for_element_to_be_visible(my_team_menu_item_locator)
        open_button_locator = self.get_open_button_locator(employee_name)
        self.wait_for_element_to_be_clickable_and_click(open_button_locator)

    @staticmethod
    def get_open_button_locator(employee_name):
        return By.XPATH, f"//td[contains(., '{employee_name}')]/ancestor::tr//a[@id='open']"

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable_and_click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator)).click()
