import pytest
from src.pages.HomePage import HomePage
from src.pages.EmployeeEvaluationPage import EmployeeEvaluationPage
import time


@pytest.fixture(scope='module')
def evaluation_page(employee_browser, config):
    # Initialize LoginPage with the browser instance provided by the 'browser' fixture
    return EmployeeEvaluationPage(employee_browser)


@pytest.mark.order(6)
def test_submit_incomplete_evaluation(employee_browser, config, evaluation_page):
    # Log in and navigate to the evaluation page as before
    home_page = HomePage(employee_browser)
    home_page.go_to_evaluation_page()
    # Instantiate the evaluation page object

    # Attempt to submit an incomplete evaluation
    evaluation_page.submit_evaluation()
    assert evaluation_page.wait_for_alert(), "Expected alert is not present after waiting"

    # Verify that an alert is present
    assert evaluation_page.is_alert_present(), "Expected alert is not present"

    # Verify that the alert text is correct
    alert_text = evaluation_page.get_alert_text()
    assert alert_text == "Please make sure that all highlighted fields are filled", \
        f"Alert text was '{alert_text}' instead of expected message."

    # Accept the alert
    evaluation_page.accept_alert()

    # Optionally, verify that the alert is no longer present
    assert not evaluation_page.is_alert_present(), "Alert did not close after accepting"


@pytest.mark.order(7)
def test_fill_evaluation_randomly(employee_browser, config, evaluation_page):
    # Log in before filling out the evaluation
    # ... (Assuming the login functionality is handled elsewhere or before this test)

    # Instantiate the home page object and navigate to the "My Evaluation" page
    # Instantiate the evaluation page object
    #evaluation_page.wait_for_overlay_button_disappear()

    # Optionally, if the overlay does not disappear, click it directly

    evaluation_page.click_overlay_button_if_present()
    time.sleep(10)
    # Fill the random ratings if applicable
    evaluation_page.fill_random_ratings()

    # Fill the evaluation form with random comments
    evaluation_page.fill_evaluation_form()
    evaluation_page.save_evaluation()
    evaluation_page.submit_evaluation()

    # Verify the form was filled (This is just a placeholder example)
    # assert "Some expected result after form fill"
