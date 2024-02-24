from src.utils.RandomDataGenerator import generate_evaluation_data


def test_empty_evaluation_not_submitted(evaluation_page):
    evaluation_page.submit_evaluation()
    assert evaluation_page.wait_for_alert(), "Expected alert is not present after waiting"
    assert evaluation_page.is_alert_present(), "Expected alert is not present"
    alert_text = evaluation_page.get_alert_text()
    assert alert_text == "Please make sure that all highlighted fields are filled", \
        f"Alert text was '{alert_text}' instead of expected message."
    evaluation_page.accept_alert()
    assert not evaluation_page.is_alert_present(), "Alert did not close after accepting"


def test_fill_evaluation_with_ratings_only_not_submitted(evaluation_page):
    evaluation_data = generate_evaluation_data()
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


def test_fill_evaluation_without_ratings_not_submitted(evaluation_page):
    evaluation_data = generate_evaluation_data()
    evaluation_page.fill_comments_evaluation_form(
        evaluation_data['like'],
        evaluation_data['dislike'],
        evaluation_data['suggestion'])
    evaluation_page.save_evaluation()
    expected_title = "Employee Evaluation"
    actual_title = evaluation_page.get_employee_page_title()
    assert actual_title == expected_title, \
        f"Page title is incorrect. Expected: '{expected_title}', Got: '{actual_title}'"


def test_submit_complete_evaluation(evaluation_page):
    evaluation_data = generate_evaluation_data()
    evaluation_page.fill_ratings_by_indices(evaluation_data['ratings'])
    evaluation_page.fill_comments_evaluation_form(
        evaluation_data['like'],
        evaluation_data['dislike'],
        evaluation_data['suggestion'])
    evaluation_page.submit_evaluation()
    evaluation_page.confirm_submission()
    expected_title = "Employee Evaluation"
    actual_title = evaluation_page.get_employee_page_title()
    assert actual_title == expected_title, (f"Page title is incorrect. Expected: "
                                            f"'{expected_title}', Got: '{actual_title}'")
