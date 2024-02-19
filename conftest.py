import pytest
import json
import os
from src.utils.DriverFactory import DriverFactory
from src.pages.LoginPage import LoginPage
from src.pages.EvaluationPage import EvaluationPage


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
        'employee': employee_config_data,
        'manager': manager_config_data
    }

    return combined_config_data


@pytest.fixture(scope='function')
def employee_browser(config):
    browser = DriverFactory.get_driver(config['employee']['browserType'])
    browser.get(config['baseUrl'])
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def manager_browser(config):
    browser = DriverFactory.get_driver(config['manager']['browserType'])
    browser.get(config['baseUrl'])
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def login_page(employee_browser, config):
    employee_browser.get(config['baseUrl'])
    return LoginPage(employee_browser)


@pytest.fixture(scope='function')
def evaluation_page(employee_browser, config):
    return EvaluationPage(employee_browser)
