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
I have created a directory called Data that inclludes:
- BasaData.json --> have the baseURL

- EmployeeData.json
  
       * Valid credentials, which also contain the Employee Name, to enable a manager to access and assess 
      an employee's evaluation.
  
       * Invalid credentials for testing unauthorized access scenarios.
  
       * browserType option to select the desired browser for conducting employee tests.

- ManagerData.json

       * Valid credentials.
  
       * Invalid credentials for testing unauthorized access scenarios.
  
       * browserType option to select the desired browser for conducting manger tests.

- screen-sizes.json
  Contains dimensions for Desktop, Mobile, and Tablet to facilitate UI/UX testing across different device sizes.

## Use of allure
The project have a directoray called 'allure_reports' and to run the project with allure you need to run these 2 cmds
```
 pytest --alluredir=allure_reports
```
--> this will generate Allure reports in the directory
```
 allure serve allure_reports
```
--> Then allure spins up a local web server and opens the report in your default web browser. This allows you to view the test results immediately in a nicely formatted interfacehis.

![image](https://github.com/Aseel1612/Asal_Evaluation_System/assets/52132245/42471a94-71b3-48c7-8e75-0c9f443c6ccb)

![image](https://github.com/Aseel1612/Asal_Evaluation_System/assets/52132245/31f80752-636f-4b69-ba71-f5980bc49f6e)




  
