from selenium.common import NoAlertPresentException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec

from .BasePage import BasePage


class EvaluationPage(BasePage):
    PAGE_NAME = "EvaluationPage"

    def __init__(self, driver):
        super().__init__(driver)

    def is_criteria_table_displayed(self):
        return len(self.find_elements(self.PAGE_NAME, "CRITERIA_ROW_LOCATOR")) > 0

    def wait_for_criteria_table_presence(self, timeout=50):
        return self.is_elements_visible(self.PAGE_NAME, "CRITERIA_ROW_LOCATOR", timeout)

    def ensure_elements_visible(self, element_name, timeout=20) -> bool:
        return self.is_elements_visible(self.PAGE_NAME, element_name, timeout)

    def is_save_button_displayed(self):
        try:
            return self.find_element(self.PAGE_NAME, "SAVE_BUTTON_LOCATOR").is_displayed()
        except NoSuchElementException:
            return False

    def fill_ratings_by_indices(self, rating_indices):
        self.wait_for(self.PAGE_NAME, "CRITERIA_ROW_LOCATOR", condition=ec.visibility_of_any_elements_located)
        criteria_rows = self.find_elements(self.PAGE_NAME, "CRITERIA_ROW_LOCATOR")
        for index, row in enumerate(criteria_rows):
            if index < len(rating_indices):
                rating_divs = row.find_elements(*self.get_locator(self.PAGE_NAME, "RATING_DIVS_LOCATOR"))
                if rating_indices[index] < len(rating_divs):
                    rating_div = rating_divs[rating_indices[index]]
                    self.wait_for_element_to_be_clickable_by_element(rating_div)
                    rating_div.click()

    def clear_rating(self):
        criteria_rows = self.find_elements(self.PAGE_NAME, "CRITERIA_ROW_LOCATOR")

        for row in criteria_rows:
            checked_checkboxes = row.find_elements(*self.get_locator(self.PAGE_NAME, "CHECKED_RATING_DIVS_LOCATOR"))

            for checkbox in checked_checkboxes:
                checkbox.click()

    def fill_comments_evaluation_form(self, like_text, dislike_text, suggestion_text):
        self.type(self.PAGE_NAME, "LIKE_TEXTAREA_LOCATOR", like_text)
        self.type(self.PAGE_NAME, "DISLIKE_TEXTAREA_LOCATOR", dislike_text)
        self.type(self.PAGE_NAME, "SUGGESTION_TEXTAREA_LOCATOR", suggestion_text)

    def fill_comments_manager_evaluation_form(self, strengths, improvements):
        self.type(self.PAGE_NAME, "STRENGTHS_TEXTAREA_LOCATOR", strengths)
        self.type(self.PAGE_NAME, "IMPROVEMENTS_TEXTAREA_LOCATOR", improvements)

    def save_evaluation(self):
        self.click(self.PAGE_NAME, "SAVE_BUTTON_LOCATOR")

    def submit_evaluation(self):
        self.click(self.PAGE_NAME, "SUBMIT_BUTTON_LOCATOR")

    def confirm_submission(self):
        self.click(self.PAGE_NAME, "CONFIRM_SUBMIT_BUTTON_LOCATOR")

    def wait_for_alert(self, timeout=10):
        return self.wait_for_alert_presence(timeout)

    def is_alert_present(self):
        try:
            alert = self.driver.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    def get_alert_text(self):
        if self.is_alert_present():
            return self.driver.switch_to.alert.text
        return None

    def accept_alert(self):
        if self.is_alert_present():
            self.driver.switch_to.alert.accept()

    def wait_for_overlay_button_disappear(self, timeout=30):
        return not self.is_element_visible(self.PAGE_NAME, "SCROLL_TO_TOP_BUTTON_LOCATOR", timeout)

    def click_overlay_button_if_present(self):
        if self.is_element_visible(self.PAGE_NAME, "SCROLL_TO_TOP_BUTTON_LOCATOR"):
            self.click(self.PAGE_NAME, "SCROLL_TO_TOP_BUTTON_LOCATOR")
        else:
            print("Overlay button not present or not visible.")

    # this is for submitting without ratings
    def get_modal_dialog_text(self):
        self.wait_for(self.PAGE_NAME, "MODAL_DIALOG_BOX_LOCATOR")
        return self.find_element(self.PAGE_NAME, "MODAL_DIALOG_TEXT_LOCATOR").text

    def confirm_modal_dialog(self):
        self.click(self.PAGE_NAME, "MODAL_CONFIRM_BUTTON_LOCATOR")

    def cancel_modal_dialog(self):
        self.click(self.PAGE_NAME, "MODAL_CANCEL_BUTTON_LOCATOR")

    def get_employee_page_title(self):
        try:
            page_title_element = self.find_element(self.PAGE_NAME, "EMPLOYEE_PAGE_TITLE_LOCATOR")
            return page_title_element.text.strip()
        except NoSuchElementException:
            return None

    def get_evaluation_period_date(self):
        try:
            evaluation_cycle_element = self.wait_for(self.PAGE_NAME, "EVALUATION_CYCLE_DATE_LOCATOR")
            full_text = evaluation_cycle_element.text.strip()
            date_part = full_text.split(":")[1].strip() if ':' in full_text else None
            return date_part
        except Exception as e:
            print(f"Error retrieving evaluation period date. Exception: {e}")
            return None

    def get_manager_page_title(self):
        try:
            page_title_element = self.find_element(self.PAGE_NAME, "PAGE_TITLE_AFTER_OPEN_BUTTON")
            return page_title_element.text.strip()
        except NoSuchElementException:
            return None
