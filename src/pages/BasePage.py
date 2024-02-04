from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator)
            )
            return element
        except TimeoutException as e:
            raise TimeoutException(f"Timed out waiting for element with locator {locator}") from e

    def find_elements(self, locator, timeout=20):
        try:
            return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))
        except TimeoutException as e:
            raise TimeoutException(f"Timed out waiting for elements with locator {locator}") from e

    def click(self, locator):
        element = self.find_element(locator)
        if element:
            element.click()
        else:
            raise NoSuchElementException(f"Element with locator {locator} not found")

    def type(self, locator, text):
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            raise NoSuchElementException(f"Element with locator {locator} not found")
