from src.pages.BasePage import BasePage
from src.locators.Locators import Locators


class HomePage(BasePage, Locators):

    def go_to_evaluation_page(self):
        self.click(self.MY_EVALUATION_LINK)

    def go_to_evaluation_history(self):
        self.click(self.MY_EVALUATION_HISTORY)

    def go_to_my_team(self):
        self.click(self. MY_TEAM_MENU_ITEM)

    def check_page_title(self):
        TITLE = self.wait_for(self.TITLE_OF_PAGE)
        return TITLE

    def is_my_team_visible(self):
        return self.is_element_visible(self.MY_TEAM_MENU_ITEM, timeout=10)
