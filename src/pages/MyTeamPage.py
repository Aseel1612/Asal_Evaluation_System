from selenium.webdriver.common.by import By
from src.pages.BasePage import BasePage
from src.locators.Locators import Locators


def get_open_button_locator(employee_name):
    return By.XPATH, f"//td[contains(., '{employee_name}')]/ancestor::tr//a[@id='open']"


class MyTeamPage(BasePage, Locators):

    def open_employee_evaluation(self, employee_name):
        if not self.is_element_visible(self.MY_TEAM_MENU_ITEM, timeout=10):
            raise Exception("My Team menu item is not visible.")

        open_button_locator = get_open_button_locator(employee_name)

        if self.is_element_clickable(open_button_locator, timeout=10):
            self.click(open_button_locator)
        else:
            raise Exception(f"Open button for employee '{employee_name}' is not clickable or not found.")
