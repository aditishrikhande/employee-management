# Employee Management CLI

## 1. Project Overview
The Employee Management CLI is a Python-based command-line
application used to manage employee records.

## 2. Problem Statement
Managing employee information manually can be difficult.
This application helps users add, update, search, delete,
and view employee records through a simple menu.

## 3. Features
- Add employee
- Update employee
- Delete employee
- Search employee by ID
- List all employees
- Find employee with the highest salary
- Calculate average salary
- Filter employees by department

## 4. Technology Stack
- Python 3.13
- PyCharm IDE

## 5. How to Run
1. Open the project in PyCharm.
2. Open main.py.
3. Right-click in the editor.
4. Select Run 'main'.
5. Choose an option from the menu.

## 6. Data Storage
Employee records are stored in memory while the application
is running. The records are not retained after exiting.

## 7. Testing
The application is tested using sample employee records.
Each menu option should be checked before submission.

## 8. Challenges and Solutions
Challenge: Preventing duplicate employee IDs.
Solution: Check whether the ID already exists before adding
a new employee.

Challenge: Handling invalid salary input.
Solution: Use exception handling to validate numeric input.

## 9. Future Improvements
- Store employee records in a JSON file.
- Add automated unit tests.
- Improve input validation.
-