from datetime import datetime

from selenium.common import NoSuchElementException, TimeoutException

from src.locators.Locators import Locators
from src.pages.BasePage import BasePage


class EvaluationHistoryPage(BasePage, Locators):

    def get_history_page_title(self):
        try:
            page_title_element = self.find_element(self.HISTORY_PAGE_TITLE)
            return page_title_element.text.strip()
        except NoSuchElementException:
            return None

    def search_in_history_table(self, text):
        search_input = self.find_element(self.SEARCH_INPUT_LOCATOR)
        search_input.clear()
        search_input.send_keys(text)

    def get_evaluation_entries(self):
        self.is_element_visible(self.HISTORY_TABLE_WRAPPER)
        return self.find_elements(self.EVALUATION_ROWS)

    def get_evaluation_details(self, evaluation_entry):
        cycle = evaluation_entry.find_element(*self.EVALUATION_CYCLE_COLUMN).text
        status = evaluation_entry.find_element(*self.EVALUATION_STATUS_COLUMN).text
        return cycle, status

    def evaluations_are_chronological(self, evaluation_entries):
        dates = [self.get_evaluation_details(entry)[0] for entry in evaluation_entries]
        parsed_dates = [datetime.strptime(date, "%B %Y") for date in dates]
        sorted_dates = sorted(parsed_dates, reverse=True)
        return parsed_dates == sorted_dates

    def view_closed_evaluation_entry(self):
        self.search_in_history_table("Closed")
        evaluation_entries = self.get_evaluation_entries()

        for entry in evaluation_entries:
            cycle, status = self.get_evaluation_details(entry)

            if status.lower() == 'closed':
                try:
                    if self.is_element_clickable(self.VIEW_BUTTON_LOCATOR):
                        self.click(self.VIEW_BUTTON_LOCATOR)
                        return True
                except TimeoutException:
                    print("The 'View' button for the closed evaluation entry is not clickable.")
                    return False
        print("No closed evaluation entries found.")
        return False
