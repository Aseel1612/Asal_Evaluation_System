def test_empty_evaluation_not_submitted(employee_evaluation_page):
    employee_evaluation_page.submit_evaluation()
    employee_evaluation_page.wait_for_alert()
    employee_evaluation_page.is_alert_present()
    alert_text = employee_evaluation_page.get_alert_text()
    assert alert_text == "Please make sure that all highlighted fields are filled", \
        f"Alert text was '{alert_text}' instead of expected message."


def test_fill_evaluation_with_ratings_only_not_submitted(ratings_filled_evaluation_form):
    ratings_filled_evaluation_form.submit_evaluation()
    ratings_filled_evaluation_form.wait_for_alert()
    alert_text = ratings_filled_evaluation_form.get_alert_text()
    ratings_filled_evaluation_form.accept_alert()
    assert (alert_text == "Please make sure that all highlighted fields are filled"
            and not ratings_filled_evaluation_form.is_alert_present()), \
        f"Alert text was '{alert_text}' or alert did not close after accepting"


def test_fill_evaluation_with_comments_only_not_submitted(comments_filled_employee_evaluation_form, ):
    comments_filled_employee_evaluation_form.save_evaluation()
    expected_title = "Employee Evaluation"
    actual_title = comments_filled_employee_evaluation_form.get_employee_page_title()
    assert actual_title == expected_title, \
        f"Page title is incorrect. Expected: '{expected_title}', Got: '{actual_title}'"


def test_submit_complete_evaluation(complete_employee_evaluation_form):
    complete_employee_evaluation_form.submit_evaluation()
    complete_employee_evaluation_form.confirm_submission()
    actual_title = complete_employee_evaluation_form.get_employee_page_title()
    assert actual_title == "Employee Evaluation", \
        f"Page title is incorrect. Expected: 'Employee Evaluation', Got: '{actual_title}'"
