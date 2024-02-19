from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from src.utils.LocatorManager import LocatorManager  # Make sure this import matches your project structure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.locator_manager = LocatorManager()

    def refresh_page(self):
        self.driver.refresh()

    def get_locator(self, page_name, element_name):
        return self.locator_manager.get_locator(page_name, element_name)

    def wait_for(self, page_name, element_name, timeout=20, condition=ec.presence_of_element_located):
        locator = self.get_locator(page_name, element_name)
        try:
            return WebDriverWait(self.driver, timeout).until(condition(locator))
        except TimeoutException as e:
            raise TimeoutException(
                f"Timed out waiting for condition on element: {element_name} on page: {page_name}") from e

    def find_element(self, page_name, element_name, timeout=20) -> WebElement:
        return self.wait_for(page_name, element_name, timeout, ec.presence_of_element_located)

    def find_elements(self, page_name, element_name, timeout=20):
        locator = self.get_locator(page_name, element_name)
        return self.wait_for(page_name, element_name, timeout, ec.presence_of_all_elements_located)

    def click(self, page_name, element_name, timeout=20):
        element = self.wait_for(page_name, element_name, timeout, ec.element_to_be_clickable)
        element.click()

    def type(self, page_name, element_name, text, timeout=20):
        element = self.find_element(page_name, element_name, timeout)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, page_name, element_name, timeout=20) -> bool:
        try:
            self.wait_for(page_name, element_name, timeout, ec.visibility_of_element_located)
            return True
        except TimeoutException:
            return False

    def is_elements_visible(self, page_name, element_name, timeout=20) -> bool:
        try:
            self.wait_for(page_name, element_name, timeout, ec.visibility_of_all_elements_located)
            return True
        except TimeoutException:
            return False

    def is_element_clickable(self, page_name, element_name, timeout=20) -> bool:
        try:
            self.wait_for(page_name, element_name, timeout, ec.element_to_be_clickable)
            return True
        except TimeoutException:
            return False

    def wait_for_alert_presence(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(ec.alert_is_present())
            return self.driver.switch_to.alert
        except TimeoutException as e:
            raise TimeoutException("Timed out waiting for the alert to be present.") from e

    def get_page_title(self):
        return self.driver.title
