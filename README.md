# Asal Evaluation System
The Asal Evaluation System simplifies how employee performance reviews are conducted. Each employee has a supervisor who assesses their work. The system is designed to be clear and fair, helping employees understand how they're doing and where they can improve.

## Set up and installation
- Install Python and pip.
- Download and install PyCharm from the JetBrains website and create a new project.
- Install Dependencies
  ```
  * pip install pytest
  ```
  ```  
  * pip install allure-pytest
  ```  

## System Data
I have created a directory called Data that includes:

- BasaData.json --> have the baseURL

- EmployeeData.json
  
       * Valid credentials, which also contain the Employee Name, to enable a manager to access and assess 
         an employee's evaluation.
  
       * Invalid credentials for testing unauthorized access scenarios.
  
       * browserType option to select the desired browser for conducting employee tests.

- ManagerData.json

       * Valid credentials.
  
       * Invalid credentials for testing unauthorized access scenarios.
  
       * browserType option to select the desired browser for conducting manager tests.
  
- Locators.json
  
  Contains all needed locators to find and interact with web elements.

- screen-sizes.json
  
  Contains dimensions for Desktop, Mobile, and Tablet to facilitate UI/UX testing across different device sizes (this has been implemented for the login page only and a 
  screenshots will be svaed to 'screenshots' directory).

## System directories overview

- conftest.py
 
  This conftest.py file is a central place to manage fixtures for testing a web application that involves employee and manager evaluations. The fixtures are organized to 
  support different stages of testing, from setting up browser instances to filling out and submitting evaluation forms.
  
- src

  * pages: this subdirectory contains Page Object Models, which are Python classes that represent web pages or components of web pages. Each class encapsulates the page 
    structure and behaviors, providing methods to interact with the web page elements such as BasePage, LoginPage, EvaluationPage, EvaluationHistoryBage, HomePage and 
    MyTeamPage.

  * utils: this subdirectory is typically used for utility classes or functions that provide common services throughout the application. It includes:
    - DriverFactory.py: provides a mechanism to instantiate different web browser drivers. It uses a pattern known as a Factory pattern to create browser instances for 
      Chrome, Firefox, and Edge, depending on which browser type is requested.
    - LocatorManager.py: used for managing locators for elements on the web pages, which can be used across various page objects.
    - RandomDataGenerator.py: a utility for generating random data that can be used for testing purposes, such as filling forms with unique information each time a test is 
      run.
    
- tests
 
  * test_employee: This subdirectory holds all the test cases related to employee interactions within the application.
    - test_EmployeeLogin.py: contains tests related to the employee login process, checking if the login functionality is working as expected.
    - test_EmployeeEvaluation.py: here tests are designed to ensure the integrity of the evaluation process. They check that an evaluation form can't be 
                                  submitted unless all required fields are filled out, that alerts for incomplete forms are displayed and can be closed, and that a 
                                  complete form can be submitted correctly. Essentially, these tests make sure that the system responds properly whether the form is filled 
                                  out partially, incorrectly, or completely.
    - test_EmployeeEvaluationHistory.py: here tests verify that the history of evaluations is displayed correctly, ensuring that entries are in the right 
                                         order, can be found for specific evaluation periods.
      
  * test_manager:This subdirectory is intended for test scripts that validate the manager's perspective of the application.
    - test_EmployeeLogin.py: contains tests related to the manager login process, checking if the login functionality is working as expected.
    - test_EmployeeEvaluation.py: here tests check the functionality of the manager's ability to complete evaluations. They ensure that an evaluation with 
                                  missing information can't be submitted, that appropriate alerts show up when the evaluation is incomplete, and that a fully filled-out 
                                  evaluation can be successfully submitted. These tests help maintain the quality of the evaluation process by verifying that all necessary 
                                  parts of the evaluation are completed before submission.


  
## Use of allure
The project have a directoray called 'allure_reports' and to run the project with allure you need to run these 2 cmds
```
 pytest --alluredir=allure_reports
```
--> this will generate Allure reports in the directory
```
 allure serve allure_reports
```
--> Then allure spins up a local web server and opens the report in your default web browser. This allows you to view the test results immediately in a nicely formatted interfaces.

![image](https://github.com/Aseel1612/Asal_Evaluation_System/assets/52132245/42471a94-71b3-48c7-8e75-0c9f443c6ccb)

![image](https://github.com/Aseel1612/Asal_Evaluation_System/assets/52132245/31f80752-636f-4b69-ba71-f5980bc49f6e)




## How to run the project
1. Clone the Repository:
  ```
  git clone https://github.com/Aseel1612/Asal_Evaluation_System.git
  ```
2. Navigate to the Project Directory:
  ```
  cd Asal_Evaluation_System
  ```   
3. Create a Virtual Environment:
  ```
  python -m venv venv
  ```
4. Activate the Virtual Environment:
  ```
  .\venv\Scripts\activate
  ```
5. Install Dependencies:
  ```
  pip install -r requirements.txt
  ```
6. Run Tests with Pytest:
  ```
  pytest --clean-alluredir --alluredir allure-results
  allure serve allure_reports
  ```
  If you want to test a specific directory or file, you can specify it like pytest tests/ or pytest tests/test_EmployeeLogin.py.


  

  
