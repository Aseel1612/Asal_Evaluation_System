from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


class DriverFactory:
    @staticmethod
    def get_driver(browser_type):
        browser_type = browser_type.lower()
        if browser_type == 'chrome':
            return DriverFactory._create_chrome_driver()
        elif browser_type == 'firefox':
            return DriverFactory._create_firefox_driver()
        elif browser_type == 'edge':
            return DriverFactory._create_edge_driver()
        else:
            raise Exception(f"Unsupported browser: {browser_type}")

    @staticmethod
    def _create_chrome_driver():
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=chrome_service, options=chrome_options)

    @staticmethod
    def _create_firefox_driver():
        firefox_options = FirefoxOptions()
        firefox_service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=firefox_service, options=firefox_options)

    @staticmethod
    def _create_edge_driver():
        edge_options = EdgeOptions()
        edge_options.use_chromium = True

        edge_options.add_argument("--disable-features=msEdgeEnterpriseRealtimeExtension")
        edge_options.add_argument("--disable-extensions")
        edge_options.add_argument("--start-maximized")
        edge_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        edge_service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=edge_service, options=edge_options)
