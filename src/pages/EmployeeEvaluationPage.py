import string
from selenium.webdriver.common.by import By
import random
from .BasePage import BasePage


class EmployeeEvaluationPage(BasePage):
    # Updated locators
    CRITERIA_ROW_LOCATOR = (By.CSS_SELECTOR, "#assets-data-table tbody tr")
    RATING_DIVS_LOCATOR = (By.CSS_SELECTOR, "td div.checker")
    # Define locators based on the HTML attributes of the text areas
    like_textarea_locator = (By.ID, "Likes")  # Update with the actual locator
    dislike_textarea_locator = (By.ID, "Dislikes")  # Update with the actual locator
    suggestion_textarea_locator = (By.ID, "Improvements")  # Update with the actual locator
    SAVE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[id='saveButton']")  # Update with the actual CSS selector
    SUBMIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[id='submitbtn']")  # Update with the actual CSS selector

    def fill_random_ratings(self):
        # Fetch all the rows for the criteria within the specific table
        criteria_rows = self.find_elements(self.CRITERIA_ROW_LOCATOR)

        for row in criteria_rows:
            # Within the row, find all the divs with the class 'checker'
            rating_divs = row.find_elements(*self.RATING_DIVS_LOCATOR)
            if rating_divs:
                # Randomly choose one of the divs and click it
                random_div = random.choice(rating_divs)
                # Click on the selected div directly
                random_div.click()

    @staticmethod
    def generate_random_text(length=50):
        """Generate a random string of fixed length."""
        letters = string.ascii_letters + string.digits + ' '
        return ''.join(random.choice(letters) for _ in range(length))

    def fill_evaluation_form(self):
        # Use the `type` method from `BasePage` to fill in the text areas with random text
        self.type(self.like_textarea_locator, self.generate_random_text())
        self.type(self.dislike_textarea_locator, self.generate_random_text())
        self.type(self.suggestion_textarea_locator, self.generate_random_text())

    def save_evaluation(self):
        # Use the `click` method from `BasePage` to click the Save button
        self.click(self.SAVE_BUTTON_LOCATOR)

    def submit_evaluation(self):
        # Use the `click` method from `BasePage` to click the Submit button
        self.click(self.SUBMIT_BUTTON_LOCATOR)
