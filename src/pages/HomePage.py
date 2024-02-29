from selenium.common import NoSuchElementException

from src.pages.BasePage import BasePage


class HomePage(BasePage):
    PAGE_NAME = "HomePage"

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_evaluation_page(self):
        self.click(self.PAGE_NAME, "MY_EVALUATION_LINK")

    def go_to_evaluation_history(self):
        self.click(self.PAGE_NAME, "MY_EVALUATION_HISTORY")

    def go_to_my_team(self):
        self.click(self.PAGE_NAME, "MY_TEAM_MENU_ITEM")

    def check_page_title(self):
        try:
            page_title_element = self.find_element(self.PAGE_NAME, "TITLE_OF_PAGE")
            return page_title_element.text.strip()
        except NoSuchElementException:
            return None

    def is_my_team_visible(self):
        return self.is_element_visible(self.PAGE_NAME, "MY_TEAM_MENU_ITEM", timeout=10)
