# Task Description: Framework Development
### Objective: You are required to build a test automation framework from scratch using Python and `pytest`. The framework should support both UI and API testing. Additionally, you'll implement Docker support for running tests in a containerized environment.

## Task Overview

### Part 1: Framework Setup

#### Framework Requirements
- The framework should support **both API and UI test layers**.
- Follow best practices for project structure, including:
  - A `conftest.py` for fixtures and reusable components.
  - Proper configuration management (e.g., base URLs, credentials, environment settings).
  - Think about logging.
  - Proper API responses validation.

#### Identifying Key Scenarios
- Determine which **key test scenarios** (UI, API, etc.) should be prioritized first.
- Provide a brief explanation of why these scenarios are critical for the automation project

### Part 2: UI Automation

#### Task: Write a simple UI test to log in and remove a user account.

##### Requirements:
- Implement a **Page Object Model (POM)**.
 - Create `LoginPage` and `UserManagementPage` classes.
  - Implement methods for logging in and removing a user.

- **Test Case**: `test_remove_user`
  - Log in with valid credentials.
  - Navigate to the account management section.
  - Remove the user account.
  - Verify that the user cannot log in after the account is deleted.

##### Tools:
- Use **Selenium WebDriver** for browser automation.

### Part 3: API Testing

#### Task: Write API tests to add and remove users, and implement JSON schema validation.

##### API Endpoints:
- `POST /api/users`: Add a new user.
- `DELETE /api/users/{id}`: Remove an existing user.

##### Requirements:
- **Test Cases**:
  - `test_add_user`: Add a user via `POST /api/users` and validate the response using JSON schema validation.
  - `test_remove_user`: Remove a user via `DELETE /api/users/{id}` and ensure the user is successfully deleted.

### Part 4: Docker Integration

#### Task: Add a `Dockerfile` for running tests in a Docker container.

##### Requirements:
- Create a `Dockerfile` that sets up an environment capable of running both UI and API tests (google can be used).
- The container should include:
  - Python.
  - Selenium WebDriver and browser drivers (or a headless browser like Chrome).

##### Docker Test Execution:
- Ensure that the UI/API tests can be run inside the container with a **single command** (e.g., `docker run`).
- Provide instructions for running the tests inside Docker, including any setup or teardown steps.

### Bonus Tasks:
1. **Parallel Execution**: Configure the framework to support running tests in parallel.


## Deliverables
1. A fully implemented **test automation framework**.
2. **UI and API test cases** including:
   - `test_remove_user` for both UI and API.
3. A `Dockerfile` for running the tests in a container.
4. A **brief document** that includes:
   - Explanation of the framework structure.
   - Key test scenarios and why they were prioritized.
   - Instructions for running tests locally and in Docker.
   - Any assumptions or limitations.

