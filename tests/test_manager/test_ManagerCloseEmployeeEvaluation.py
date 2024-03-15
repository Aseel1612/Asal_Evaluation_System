def test_close_evaluation(manager_evaluation_page):
    manager_evaluation_page.close_evaluation()
    manager_evaluation_page.confirm_close()
    actual_title = manager_evaluation_page.get_employee_page_title()
    assert actual_title == "Supervisor Evaluation", \
        f"Page title is incorrect. Expected: 'Supervisor Evaluation', Got: '{actual_title}'"