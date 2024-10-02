# Task Description: API Testing and Entity Management
### Objective: You will be required to complete two parts in this task: one focusing on UI automation with Selenium and another on API testing. Additionally, you will implement logic to handle entity removal and test data management.


### Part 1: UI Automation (Selenium)
Scenario: We have a login page that allows users to log in and manage their accounts. <br/>
Your task is to implement the missing functions in the LoginPage class and write corresponding tests in test_login.py

#### User Management
1. Configure WebDriver setup in conftest.py
1. Implement the methods inside the LoginPage class for interacting with web elements.
1. Complete the following test cases in the test_login.py:
    - test_valid_login: Test a valid login scenario.
    - test_invalid_login: Test an invalid login scenario.
    - implement test_account_removal test: User removes its own account

## Part 2: API Testing (REST API)
Scenario: You are working with a REST API that manages user accounts. Your task is to implement tests for various API endpoints related to user management and entity management. <br/>
https://demoqa.com/swagger/#/BookStore/BookStoreV1BookGet

API Endpoints:
1. GET /BookStore/v1/Books
2. POST /BookStore/v1/Books
3. DELETE /BookStore/v1/Books
4. GET /BookStore/v1/Book
    
    
#### Write API Tests:
Implement tests for the following scenarios using a testing framework like pytest :
1. test_create_book: Test user creation via the POST /api/users endpoint.
1. test_get_books: Test fetching a user’s details with the GET /api/users/{id} endpoint.
1. test_get_book: Test fetching a user’s details with the GET /api/users/{id} endpoint.
1. test_update_user: Test updating a user’s information using the PUT /api/users/{id} endpoint.

### Data Cleanup:
    - Implement logic to ensure that any test data created during testing is removed after the tests run.
    - Ensure the tests are idempotent, meaning they can be executed multiple times without side effects on the test data.
    - Handle potential race conditions where the test data could be in an unexpected state.
