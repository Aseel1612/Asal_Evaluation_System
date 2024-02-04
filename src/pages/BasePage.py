from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for(self, locator, timeout=20, condition=ec.presence_of_element_located):
        try:
            return WebDriverWait(self.driver, timeout).until(condition(locator))
        except TimeoutException as e:
            raise TimeoutException(f"Timed out waiting for condition on element with locator {locator}") from e

    def find_element(self, locator, timeout=20) -> WebElement:
        return self.wait_for(locator, timeout, ec.presence_of_element_located)

    def find_elements(self, locator, timeout=20):
        return self.wait_for(locator, timeout, ec.presence_of_all_elements_located)

    def click(self, locator, timeout=20):
        element = self.wait_for(locator, timeout, ec.element_to_be_clickable)
        element.click()

    def type(self, locator, text, timeout=20):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator, timeout=20) -> bool:
        try:
            self.wait_for(locator, timeout, ec.visibility_of_element_located)
            return True
        except TimeoutException:
            return False

    def is_element_clickable(self, locator, timeout=20) -> bool:
        try:
            self.wait_for(locator, timeout, ec.element_to_be_clickable)
            return True
        except TimeoutException:
            return False

    def wait_for_alert_presence(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(ec.alert_is_present())
            return self.driver.switch_to.alert
        except TimeoutException as e:
            raise TimeoutException("Timed out waiting for the alert to be present.") from e