import pytest

from src.pages.EvaluationPage import EvaluationPage
from src.pages.HomePage import HomePage
from src.pages.MyTeamPage import MyTeamPage
from src.DataGenrator.data_generator import generate_manager_evaluation_data


@pytest.fixture(scope='module')
def evaluation_manager_page(manager_browser, config):
    return EvaluationPage(manager_browser)


@pytest.mark.order(3)
def test_open_employee_evaluation_from_the_manager_side(manager_browser, config, evaluation_manager_page):
    home_page = HomePage(manager_browser)
    home_page.go_to_my_team()
    my_team_page = MyTeamPage(manager_browser)
    employee_name = config['employee']['valid_credentials']['EmployeeName']
    my_team_page.open_employee_evaluation(employee_name)
    evaluation_manager_page.is_criteria_table_displayed()
    assert evaluation_manager_page.wait_for_criteria_table_presence(), "Criteria table is not visible."


@pytest.mark.order(4)
def test_fill_evaluation_randomly(manager_browser, config, evaluation_manager_page):
    evaluation_data = generate_manager_evaluation_data()
    evaluation_manager_page.fill_ratings_by_indices(evaluation_data['ratings'])
    evaluation_manager_page.fill_comments_manager_evaluation_form(
        evaluation_data['strengths'],
        evaluation_data['improvements'])
    evaluation_manager_page.save_evaluation()
    evaluation_manager_page.submit_evaluation()
    evaluation_manager_page.confirm_submission()
    expected_title = "Supervisor Evaluation"
    actual_title = evaluation_manager_page.get_manager_page_title()
    assert actual_title == expected_title, (f"Page title is incorrect. Expected:"
                                            f" '{expected_title}', Got: '{actual_title}'")
