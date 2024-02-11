import pytest

from src.pages.EvaluationPage import EvaluationPage
from src.pages.HomePage import HomePage
from src.pages.EvaluationHistoryPage import EvaluationHistoryPage


@pytest.fixture(scope='module')
def evaluation_history_page(employee_browser, config):
    return EvaluationHistoryPage(employee_browser)


@pytest.mark.order(10)
def test_open_history_page(employee_browser, config, evaluation_history_page):
    home_page = HomePage(employee_browser)
    home_page.go_to_evaluation_history()
    expected_title = "Employee History"
    actual_title = evaluation_history_page.get_history_page_title()
    assert actual_title == expected_title, (f"Page title is incorrect. Expected:"
                                            f" '{expected_title}', Got: '{actual_title}'")


@pytest.mark.order(11)
def test_evaluations_are_chronological(employee_browser, config, evaluation_history_page):
    evaluation_entries = evaluation_history_page.get_evaluation_entries()
    assert evaluation_history_page.evaluations_are_chronological(evaluation_entries), \
        "Evaluations are not displayed in chronological order."


@pytest.mark.order(12)
def test_search_currently_cycle(employee_browser, config, evaluation_history_page):
    evaluation_page = EvaluationPage(employee_browser)
    text = evaluation_page.get_evaluation_period_date()
    evaluation_history_page.search_in_history_table(text)
    evaluation_entries = evaluation_history_page.get_evaluation_entries()
    assert evaluation_entries, f"No evaluation entries found for the cycle '{text}'."


@pytest.mark.order(13)
def test_view_closed_evaluation(evaluation_history_page):
    is_viewed = evaluation_history_page.view_closed_evaluation_entry()
    assert is_viewed, "No closed evaluation entry was found or the 'View' button was not clickable."
