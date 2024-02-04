import time

import pytest

from src.pages.EvaluationPage import EmployeeEvaluationPage
from src.pages.HomePage import HomePage
from src.pages.MyTeamPage import MyTeamPage
from src.pages.data_generator import generate_manager_evaluation_data


@pytest.fixture(scope='module')
def evaluation_page(employee_browser, config):
    return EmployeeEvaluationPage(employee_browser)


@pytest.mark.order(3)
def test_fill_evaluation_randomly(manager_browser, config, evaluation_page):
    home_page = HomePage(manager_browser)
    home_page.go_to_my_team()  # Navigates to "My Team"

    my_team_page = MyTeamPage(manager_browser)
    employee_name = config['employee']['valid_credentials']['name']
    my_team_page.open_employee_evaluation(employee_name)
    time.sleep(10)
    evaluation_data = generate_manager_evaluation_data()
    evaluation_page.fill_ratings_by_indices(evaluation_data['ratings'])
    evaluation_page.fill_comments_manager_evaluation_form(
        evaluation_data['strengths'],
        evaluation_data['improvements'])
    evaluation_page.save_evaluation()
