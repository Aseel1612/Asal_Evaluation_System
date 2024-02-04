import time

import pytest

from src.pages.EvaluationPage import EmployeeEvaluationPage
from src.pages.HomePage import HomePage
from src.pages.MyTeamPage import MyTeamPage
from src.pages.data_generator import generate_manager_evaluation_data


@pytest.fixture(scope='module')
def evaluation_manager_page(employee_browser, config):
    return EmployeeEvaluationPage(employee_browser)


@pytest.mark.order(3)
def test_fill_evaluation_randomly(manager_browser, config, evaluation_manager_page):
    home_page = HomePage(manager_browser)
    home_page.go_to_my_team()

    my_team_page = MyTeamPage(manager_browser)
    employee_name = config['employee']['valid_credentials']['name']
    my_team_page.open_employee_evaluation(employee_name)

    # Replace time.sleep with an explicit wait
    assert evaluation_manager_page.wait_for_criteria_table_presence(), "Criteria table is not visible."

    evaluation_data = generate_manager_evaluation_data()
    evaluation_manager_page.fill_ratings_by_indices(evaluation_data['ratings'])
    evaluation_manager_page.fill_comments_manager_evaluation_form(
        evaluation_data['strengths'],
        evaluation_data['improvements'])
    evaluation_manager_page.save_evaluation()

