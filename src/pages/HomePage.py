from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    MY_EVALUATION_LINK = (By.CSS_SELECTOR, "a[href='/Employee/EvaluationView']")
    MY_EVALUATION_HISTORY = (By.CSS_SELECTOR, "a[href='/Employee/EvaluationHistory']")
    MY_TEAM_MENU_ITEM = (By.XPATH, "//a[@href='/Supervisor/getEmployees']")

    def go_to_evaluation_page(self):
        self.click(self.MY_EVALUATION_LINK)

    def go_to_evaluation_history(self):
        self.click(self.MY_EVALUATION_HISTORY)

    def go_to_my_team(self):
        self.click(self. MY_TEAM_MENU_ITEM)

    def is_my_team_visible(self):
        return self.is_element_visible(self.MY_TEAM_MENU_ITEM, timeout=10)

    def open_employee_evaluation(self, employee_name):
        # Wait for the 'My Team' section to be visible
        self.is_element_visible(self.MY_TEAM_MENU_ITEM, timeout=10)

        # Build a dynamic locator for the employee's "Open" button
        open_button_locator = (By.XPATH, f"//td[contains(., '{employee_name}')]/following-sibling::td//a[@id='open']")