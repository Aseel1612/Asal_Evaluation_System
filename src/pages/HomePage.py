# pages/HomePage.py

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    MY_EVALUATION_LINK = (By.CSS_SELECTOR, "a[href='/Employee/EvaluationView']")
    MY_EVALUATION_HISTORY = (By.CSS_SELECTOR, "a[href='/Employee/EvaluationView']")

    def go_to_evaluation_page(self):
        self.click(self.MY_EVALUATION_LINK)
