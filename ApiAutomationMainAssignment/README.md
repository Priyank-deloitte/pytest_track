# API Automation - Notes API / Main Assignment

Performed Backend API Automation Testing for Notes application APIs.
Visit application at - https://practice.expandtesting.com/notes/app

Base URL = https://practice.expandtesting.com/notes/api


## Installation

1. Clone the repository:

   ```shell
   https://github.com/Priyank-deloitte/pytest_track.git
2. Change into the project directory:
    ```shell
    cd PytestAssignmentMain

3. Create and activate a virtual environment:
    ```shell
    python -m venv env

    env\Scripts\activate
   
4. Package Installation:
    ```shell
    pip install pytest
   
   pip install selenium
   
   pip install allure-pytest
   
   pip install pytest-xdist

5. Install the dependencies:
    ```shell
   pip install -r requirements.txt

##Configuration
###Folder Structure
1. 
    ```shell
   PytestAssignmentMain
   
    ---Config
        -----config.py  
      
    ---JsonFiles
        -----changePassword.json
        -----createNote.json
        -----loginUser.json
        -----resgisterNewUser.json
        -----updateExistingNote.json
        -----updateUserProfile.json
   
    ---LogReport  
        -----logfile.log
   
    ---report  
        -----allureReport
   
    ---Tests
        -----conftest.py
        -----test_Health.py
        -----test_Notes.py
        -----test_Users.py
          
    ---Utilities
        -----logger.py  
   
    ---requirements.txt 
   
    ---README.md
   
2. Execute all test:
    ```shell
   pytest -v -s

2. Execute tests in parallel:
    ```shell
   pytest -n 2
   
2. Execute tests with specific marker:
    ```shell
   pytest -m "sanity"
   
2. Generate test coverage report: Allure Report:
    ```shell
    pytest -v -s --alluredir="report" {filename}.py
   