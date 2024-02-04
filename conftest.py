import pytest
import json
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(scope='session')
def screen_sizes():
    with open('Data/screen_sizes.json') as f:
        return json.load(f)


@pytest.fixture(scope='session')
def config():
    # Load the configuration from `EmployeeData.json`
    config_path = os.path.join(os.path.dirname(__file__), 'Data', 'EmployeeData.json')
    with open(config_path) as config_file:
        config_data = json.load(config_file)
    return config_data


@pytest.fixture(scope='session')
def browser(config):
    if config['browserType'].lower() == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Suppress the logging

        # Pass the ChromeService with the path from ChromeDriverManager
        chrome_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    elif config['browserType'].lower() == 'firefox':
        firefox_options = FirefoxOptions()

        # Set Firefox preferences to handle SSL errors and logging
        firefox_options.set_preference("webdriver.log.driver", "OFF")
        firefox_options.set_preference("network.http.use-cache", False)
        firefox_options.set_preference("security.insecure_field_warning.contextual.enabled", False)
        firefox_options.set_preference("security.certificate_errors.insecure_field_warning.contextual.enabled", False)

        # Pass the FirefoxService with the path from GeckoDriverManager
        firefox_service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

    elif config['browserType'].lower() == 'edge':
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Pass the EdgeService with the path from EdgeChromiumDriverManager
        edge_service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=edge_service, options=edge_options)

    else:
        raise Exception(f"Unsupported browser: {config['browserType']}")

    # Navigate to the base URL
    driver.get(config['baseUrl'])
    yield driver
    driver.quit()
