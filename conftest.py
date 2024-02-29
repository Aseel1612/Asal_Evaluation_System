import pytest
import json
import os
from src.pages.HomePage import HomePage
from src.pages.MyTeamPage import MyTeamPage
from src.utils.DriverFactory import DriverFactory
from src.pages.LoginPage import LoginPage
from src.pages.EvaluationPage import EvaluationPage
from src.utils.RandomDataGenerator import generate_evaluation_data, generate_manager_evaluation_data


@pytest.fixture(scope='session')
def screen_sizes():
    with open('Data/screen_sizes.json') as f:
        return json.load(f)


@pytest.fixture(scope='session')
def base_config():
    base_config_path = os.path.join(os.path.dirname(__file__), 'Data', 'BaseData.json')
    with open(base_config_path) as base_config_file:
        return json.load(base_config_file)


@pytest.fixture(scope='session')
def employee_config():
    employee_config_path = os.path.join(os.path.dirname(__file__), 'Data', 'EmployeeData.json')
    with open(employee_config_path) as employee_config_file:
        return json.load(employee_config_file)


@pytest.fixture(scope='session')
def manager_config():
    manager_config_path = os.path.join(os.path.dirname(__file__), 'Data', 'ManagerData.json')
    with open(manager_config_path) as manager_config_file:
        return json.load(manager_config_file)


@pytest.fixture(scope='function')
def employee_browser(base_config, employee_config):
    browser = DriverFactory.get_driver(employee_config['browserType'])
    browser.get(base_config['baseUrl'])
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def manager_browser(base_config, manager_config):
    browser = DriverFactory.get_driver(manager_config['browserType'])
    browser.get(base_config['baseUrl'])
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def employee_login_page(employee_browser, employee_config):
    return LoginPage(employee_browser, employee_config['valid_credentials'], employee_config['invalid_credentials'])


@pytest.fixture(scope='function')
def employee_evaluation_page(employee_browser, employee_login_page):
    employee_login_page.login_with_valid_credentials()
    home_page = HomePage(employee_browser)
    home_page.go_to_evaluation_page()
    evaluation_page = EvaluationPage(employee_browser)
    evaluation_page_title = evaluation_page.get_employee_page_title()
    assert evaluation_page_title == "Employee Evaluation", "The browser is not on the evaluation page."
    return evaluation_page


@pytest.fixture(scope="function")
def employee_evaluation_data():
    return generate_evaluation_data()


@pytest.fixture(scope="function")
def comments_filled_employee_evaluation_form(employee_evaluation_page, employee_evaluation_data):
    employee_evaluation_page.fill_comments_evaluation_form(
        employee_evaluation_data['like'],
        employee_evaluation_data['dislike'],
        employee_evaluation_data['suggestion'])
    return employee_evaluation_page


@pytest.fixture(scope="function")
def ratings_filled_evaluation_form(employee_evaluation_page, employee_evaluation_data):
    employee_evaluation_page.wait_for_criteria_table_presence()
    employee_evaluation_page.fill_ratings_by_indices(employee_evaluation_data['ratings'])
    return employee_evaluation_page


@pytest.fixture(scope="function")
def complete_employee_evaluation_form(employee_evaluation_page, employee_evaluation_data):
    employee_evaluation_page.wait_for_criteria_table_presence()
    employee_evaluation_page.fill_ratings_by_indices(employee_evaluation_data['ratings'])
    employee_evaluation_page.fill_comments_evaluation_form(
        employee_evaluation_data['like'],
        employee_evaluation_data['dislike'],
        employee_evaluation_data['suggestion'])
    return employee_evaluation_page


# For the manager side
@pytest.fixture(scope='function')
def manager_login_page(manager_browser, manager_config):
    return LoginPage(manager_browser, manager_config['valid_credentials'], manager_config['invalid_credentials'])


@pytest.fixture(scope='function')
def manager_evaluation_page(manager_browser, manager_login_page, employee_config):
    manager_login_page.login_with_valid_credentials()
    home_page = HomePage(manager_browser)
    home_page.go_to_my_team()
    my_team_page = MyTeamPage(manager_browser)
    employee_name = employee_config['valid_credentials']['EmployeeName']
    my_team_page.open_employee_evaluation(employee_name)
    manager_evaluation_page = EvaluationPage(manager_browser)
    evaluation_page_title = manager_evaluation_page.get_manager_page_title()
    assert evaluation_page_title == "Supervisor Evaluation", "The browser is not on the supervisor evaluation page."
    return manager_evaluation_page


@pytest.fixture(scope="function")
def manager_evaluation_data():
    return generate_manager_evaluation_data()


@pytest.fixture(scope="function")
def comments_filled_manager_evaluation_form(manager_evaluation_page, manager_evaluation_data):
    manager_evaluation_page.fill_comments_manager_evaluation_form(
        manager_evaluation_data['strengths'],
        manager_evaluation_data['improvements'])
    return manager_evaluation_page


@pytest.fixture(scope="function")
def ratings_manager_filled_evaluation_form(manager_evaluation_page, manager_evaluation_data):
    manager_evaluation_page.wait_for_criteria_table_presence()
    manager_evaluation_page.fill_ratings_by_indices(manager_evaluation_data['ratings'])
    return manager_evaluation_page


@pytest.fixture(scope="function")
def complete_manager_evaluation_form(manager_evaluation_page, manager_evaluation_data):
    manager_evaluation_page.wait_for_criteria_table_presence()
    manager_evaluation_page.fill_ratings_by_indices(manager_evaluation_data['ratings'])
    manager_evaluation_page.fill_comments_manager_evaluation_form(
        manager_evaluation_data['strengths'],
        manager_evaluation_data['improvements'])
    return manager_evaluation_page
