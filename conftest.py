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
    base_config_path = os.path.join(os.path.dirname(__file__), 'Data', 'BaseData.json')
    with open(base_config_path) as base_config_file:
        base_config_data = json.load(base_config_file)

    employee_config_path = os.path.join(os.path.dirname(__file__), 'Data', 'EmployeeData.json')
    with open(employee_config_path) as employee_config_file:
        employee_config_data = json.load(employee_config_file)

    manager_config_path = os.path.join(os.path.dirname(__file__), 'Data', 'ManagerData.json')
    with open(manager_config_path) as manager_config_file:
        manager_config_data = json.load(manager_config_file)

    combined_config_data = {
        'baseUrl': base_config_data['baseUrl'],
        'screenshotPath': os.path.join(os.path.dirname(__file__), base_config_data['screenshotPath']),
        'pageSourcePath': os.path.join(os.path.dirname(__file__), base_config_data['pageSourcePath']),
        'employee': employee_config_data,
        'manager': manager_config_data
    }

    return combined_config_data


@pytest.fixture(scope='session')
def employee_browser(config):
    browser = init_browser(config['employee']['browserType'])
    browser.get(config['baseUrl'])
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def manager_browser(config):
    browser = init_browser(config['manager']['browserType'])
    browser.get(config['baseUrl'])
    yield browser
    browser.quit()


def init_browser(browser_type):
    browser_type = browser_type.lower()
    if browser_type == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=chrome_service, options=chrome_options)
    elif browser_type == 'firefox':
        firefox_options = FirefoxOptions()
        firefox_service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=firefox_service, options=firefox_options)
    elif browser_type == 'edge':
        edge_options = EdgeOptions()
        edge_service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=edge_service, options=edge_options)
    else:
        raise Exception(f"Unsupported browser: {browser_type}")
