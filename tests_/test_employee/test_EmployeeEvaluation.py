import pytest

from src.pages.EvaluationPage import EmployeeEvaluationPage
from src.pages.HomePage import HomePage
from src.pages.data_generator import generate_evaluation_data


@pytest.fixture(scope='module')
def evaluation_page(employee_browser, config):
    return EmployeeEvaluationPage(employee_browser)


@pytest.mark.order(6)
def test_submit_empty_evaluation(employee_browser, config, evaluation_page):
    home_page = HomePage(employee_browser)
    home_page.go_to_evaluation_page()
    evaluation_page.submit_evaluation()
    assert evaluation_page.wait_for_alert(), "Expected alert is not present after waiting"

    assert evaluation_page.is_alert_present(), "Expected alert is not present"

    alert_text = evaluation_page.get_alert_text()
    assert alert_text == "Please make sure that all highlighted fields are filled", \
        f"Alert text was '{alert_text}' instead of expected message."

    evaluation_page.accept_alert()

    assert not evaluation_page.is_alert_present(), "Alert did not close after accepting"


@pytest.mark.order(7)
def test_submit_evaluation_with_ratings_only(employee_browser, config, evaluation_page):
    evaluation_data = generate_evaluation_data()
    evaluation_page.click_overlay_button_if_present()
    evaluation_page.wait_for_criteria_table_presence()
    evaluation_page.fill_ratings_by_indices(evaluation_data['ratings'])
    evaluation_page.submit_evaluation()
    assert evaluation_page.wait_for_alert(), "Expected alert is not present after waiting"

    assert evaluation_page.is_alert_present(), "Expected alert is not present"

    alert_text = evaluation_page.get_alert_text()
    assert alert_text == "Please make sure that all highlighted fields are filled", \
        f"Alert text was '{alert_text}' instead of expected message."

    evaluation_page.accept_alert()

    assert not evaluation_page.is_alert_present(), "Alert did not close after accepting"


@pytest.mark.order(8)
def test_fill_evaluation_without_ratings(employee_browser, config, evaluation_page):
    evaluation_page.wait_for_criteria_table_presence()
    evaluation_page.clear_rating()
    evaluation_data = generate_evaluation_data()
    # evaluation_page.click_overlay_button_if_present()
    evaluation_page.wait_for_criteria_table_presence()
    evaluation_page.fill_comments_evaluation_form(
        evaluation_data['like'],
        evaluation_data['dislike'],
        evaluation_data['suggestion'])
    evaluation_page.save_evaluation()
    expected_title = "Employee Evaluation"
    actual_title = evaluation_page.get_employee_page_title()
    assert actual_title == expected_title, (f"Page title is incorrect. Expected:"
                                            f" '{expected_title}', Got: '{actual_title}'")


@pytest.mark.order(9)
def test_fill_evaluation_randomly(employee_browser, config, evaluation_page):
    evaluation_data = generate_evaluation_data()
    evaluation_page.click_overlay_button_if_present()
    assert evaluation_page.wait_for_criteria_table_presence(), "Criteria table is not visible."
    evaluation_page.fill_ratings_by_indices(evaluation_data['ratings'])
    evaluation_page.fill_comments_evaluation_form(
        evaluation_data['like'],
        evaluation_data['dislike'],
        evaluation_data['suggestion'])
    evaluation_page.save_evaluation()
    expected_title = "Employee Evaluation"
    actual_title = evaluation_page.get_employee_page_title()
    assert actual_title == expected_title, (f"Page title is incorrect. Expected:"
                                            f" '{expected_title}', Got: '{actual_title}'")
