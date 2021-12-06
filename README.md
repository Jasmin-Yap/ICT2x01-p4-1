# 2x01-P4-1-WebPortal
| ID    | Name          | Role          |
| ------------- | ------------- | ------------- |
| 2002124  | ANG WEI JIE  | Team Leader, Backend Dev  |
| 2001571  | JASMIN YAP YI  | Technical Lead, Full Stack Dev  |
| 2001364  | THUR YOU FU  | Full Stack Dev  |
| 2000860  | MUHAMMAD NUR AFNAN BIN ABDUL RAHIM  | Backend Dev, Robotic Car Dev |
| 2001615  | ARIEF IRFAN BIN ZULFA  | Frontend Dev  |
## Installing Dependencies
This project runs on python Flask. For ease of installation, all required packages are listed in [requirements.txt](https://github.com/Jasmin-Yap/ICT2x01-p4-1/blob/dev/requirements.txt).

To install the packages, pip is used. If you do not have pip, please install it before continuing, you can find how to install pip [here](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/).

Use the command below to install the packages:
```
pip install -r requirements.txt
```
## How to run
1. Navigate to the Web-Portal directory in your choise of console (i.e. command prompt, powershell, etc)
2. Enter the commands below to run the flask program:
```
set FLASK_APP=server.py
flask run
```
## Development Workflow
### Feature Branches
1. Create a new branch based on dev. Naming Convention: feature/\<feature name\>
2. Develop on feature branch
3. When ready to merge with dev, pull from dev to get the latest updates and resolve any conflicts
4. After updating branch, open a pull request and request review from Technical Lead. 
     - If the request originates from Jasmin, request review from any other team member.
4. Reviewer to check if:
     1. Code is logical
     2. Program can be run without errors
     3. New changes do not "break" other features
6. If changes requested:
     1. Make changes according to review comments, clarify if unsure.
     2. Test
     3. Push code to remote branch
     4. Inform reviewer that changes have been completed
7. If pull request is approved, Technical Lead will merge pull request to dev branch.
8. All team members to update their respective branches to match dev

### Integration Branch
***Only one integration branch can be created.***
- Workflow generally follows "New Feature" workflow with the exception of the naming convention.
- Integration branch works across modules and handles the integration of features.

### Dev Branch
***Only one dev branch can be created***
- Holds the most updated code without breaking other featues.

### Main Branch (Master)
***Only one main branch can be created***
- Only merge pull requests from dev branch
- feature and integration brnaches cannot merge with main

## Blackbox Testing: User Acceptance Testing
### Blackbox Testing Video
Please find the video of blackbox test execution here &#8594; https://youtu.be/wo8pbCe2cAM

### How is the test executed?
Our Blackbox testing is done based on functional testing. This means that we will go through the web application to test on the functional requirements.
We based our tests on the test cases we have made on M2. To have a better flow and idea of the Blackbox testing, we have made an updated test case table.
The steps are elaborated through in the video.

### Updated Test Cases
| Testcase ID    | Description     | Pre-condition    | Expected Result    |
| ------------- | ------------- | ------------- | ------------- |
| 1 | Navigate to web portal  | In a web browser  |  Observe the connection page up and running.  |
| 2 | Input for establishing connection  |  In connection page  | Correct input should allow entry to dashboard, while wrong input should display an error message on specified field. |
| 3 | Establish a connection  | In connection page  | Entering the dashboard page. Being able to observe the dashboard. |
| 4 | Navigate through all pages  | In dashboard page | Navigate through the dashboard smoothly. |
| 5 | Data on dashboard (empty)  | In dashboard page  |  Observe the dashboard with no data shown or set to 0 accordingly. |
| 6 | Send Instructions to Robotic Car  | In dashboard page  | Able to send instructions through the control panel by dragging & dropping and clicking of the buttons accordingly. |
| 7 | Data on dashboard (filled/not-empty)  | In dashboard page  |  Observe the data changes on the dashboard page. |
| 8 | Creating a maze  | In maze creator page  | Able to click on the maze creation sections and create a maze when all requirements are fulfilled (Having a start point, line trail and an end point). Error message shown when maze creation lacks any requirement. |
| 9 | Viewing the scoreboard | In scoreboard page | View the scoreboard with the least amount of moves as the top score. View the different scores based on the maze. |
| 10 | Ending the connection and closing web portal | In any page with the side menu bar shown  | Observe return to connection page, exiting the page in pre-condition. |  


## Whitebox Testing: Token Controller
### Why Token Controller?
Token Controller generates and verifies the token needed to access the internal pages of the web portal.

When the connection to the Robotic Car is established, a token is generated by the Token Controller before directing the user to the dashboard page. Navigating to any page (excluding the connection page), will trigger a check to see if the token exists. If it does not exist, the user will be redirected back to the connection page. If it does exist, the user will be directed to the page they navigated to.

The token is also used to verify responses (acknowledgments) and data sent from the Robotic Car.

### How is the test executed?
The test is done in two parts. The first is automated using unittest and tests the function calls of the Token Controller. The second part is done manually by verifying the redirect on the web portal when navigating using URL paths.

### unittest
The file used for the test can be found here &#8594; https://github.com/Jasmin-Yap/ICT2x01-p4-1/blob/main/Web-Portal/token_test.py

Execution of automated whitebox testing:
![code coverage](https://github.com/Jasmin-Yap/ICT2x01-p4-1/blob/main/resources/unittest.jpg)

A Code coverage report was generated for the automated part of the test:
![code coverage](https://github.com/Jasmin-Yap/ICT2x01-p4-1/blob/main/resources/coverage-report.jpg)

### Files Involved
#### Unittest
1. https://github.com/Jasmin-Yap/ICT2x01-p4-1/blob/main/Web-Portal/token_test.py
2. https://github.com/Jasmin-Yap/ICT2x01-p4-1/blob/main/Web-Portal/models/token.py
3. https://github.com/Jasmin-Yap/ICT2x01-p4-1/blob/main/Web-Portal/controllers/token_controller.py
#### Manual
1. https://github.com/Jasmin-Yap/ICT2x01-p4-1/blob/main/Web-Portal/controllers/dashboard_controller.py &#8594; Lines 32-33 and 45-46
2. https://github.com/Jasmin-Yap/ICT2x01-p4-1/blob/main/Web-Portal/controllers/maze_controller.py &#8594; Lines 77-78
3. https://github.com/Jasmin-Yap/ICT2x01-p4-1/blob/main/Web-Portal/controllers/scoreboard_controller.py &#8594; Lines 80-81

### Whitebox Testing Execution
Please find the video of whitebox test execution here &#8594; https://youtu.be/bYw37OdO3Rs
