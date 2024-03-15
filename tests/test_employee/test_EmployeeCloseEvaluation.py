def test_close_evaluation(employee_evaluation_page):
    employee_evaluation_page.close_evaluation()
    employee_evaluation_page.confirm_close()
    actual_title = employee_evaluation_page.get_employee_page_title()
    assert actual_title == "Employee Evaluation", \
        f"Page title is incorrect. Expected: 'Employee Evaluation', Got: '{actual_title}'"