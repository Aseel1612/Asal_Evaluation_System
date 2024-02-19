from src.pages.BasePage import BasePage


class HomePage(BasePage):
    PAGE_NAME = "HomePage"

    def is_at(self):
        # Check if the browser is currently displaying the home page
        return self.is_element_visible(self.PAGE_NAME, "TITLE_OF_PAGE")

    def go_to_evaluation_page(self):
        self.click(self.PAGE_NAME, "MY_EVALUATION_LINK")

    def go_to_evaluation_history(self):
        self.click(self.PAGE_NAME, "MY_EVALUATION_HISTORY")

    def go_to_my_team(self):
        self.click(self.PAGE_NAME, "MY_TEAM_MENU_ITEM")

    def check_page_title(self):
        title_element = self.wait_for(self.PAGE_NAME, "TITLE_OF_PAGE")
        return title_element.text if title_element else None

    def is_my_team_visible(self):
        return self.is_element_visible(self.PAGE_NAME, "MY_TEAM_MENU_ITEM", timeout=10)
