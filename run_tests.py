import subprocess

test_files = [
    "tests/test_employee/test_EmployeeLogin.py",
    "tests/test_employee/test_EmployeeEvaluation.py",
    "tests/test_manager/test_ManagerLogin.py",
    "tests/test_manager/test_ManagerEvaluationForEmployee.py",
    "tests/test_manager/test_ManagerCloseEmployeeEvaluation.py",
    "tests/test_employee/test_EmployeeCloseEvaluation.py",
    "tests/test_employee/test_EmployeeEvaluationHistory.py"
]

subprocess.run(["pytest", "--clean-alluredir", "--alluredir", "allure_reports"] + test_files)

