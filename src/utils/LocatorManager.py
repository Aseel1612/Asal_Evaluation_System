
import json
import os
from selenium.webdriver.common.by import By


class LocatorManager:
    def __init__(self):
        self.locators_path = os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'Locators.json')
        with open(self.locators_path, 'r') as locators_file:
            self.locators = json.load(locators_file)

    def get_locator(self, page, element_name):
        locator_type, locator_value = self.locators[page][element_name]
        return getattr(By, locator_type.upper()), locator_value
