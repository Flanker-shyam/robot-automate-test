<h1>Robot automated testing</h1>

<h2>Description:</h2>
<p>The core objective of this challenge is to create a system that can accept a detailed API call,
execute the testing steps provided within as a Robot Framework test, and subsequently
return the test output. This entails developing an application using Python and Django that
exposes an API endpoint. This endpoint should accept a POST request structured as
follows, execute the detailed steps using the Robot Framework, and return the results</p>

<h2> Technologoies used:</h2>
<ol>
  <li>Python</li>
  <li>Django</li>
  <li>Robot Testing Framework</li>
  <li>Selenium Framework for Robot</li>
</ol>

<h2>How to Setup</h2>
<ol>
  <li>Fork this repo</li>
  <li>Clone this repo</li>
  
  ```bash
  git clone git@github.com:Flanker-shyam/irctc-mock-app.git
  ```
<li>Activte Virtual environment (optional)</li>

  ```bash
  source django/bin/activate
  ```
<li>cd to myproject directory</li>
 
  ``` bash
  cd myproject
  ```

<li>install dependencies</li>

  ```bash
  pip install -r requirements.txt
  ```
</ol>

<h3>That's pretty much of setup, let's try running this code</h3>
Type following command in your terminal

```bash
python manage.py runserver
```

Let's test the endpoints for automate robot test
Open you postman and create a post request to the following mentioned endpoints:

``` bash
http://localhost:8000/testai/tests/v1/execute
```

Copy data from "dummy_tests.txt" to the body of your post request in postman
and hit run

<p>You will see some automatic magic happening in your computer, just let them happen (voilaaa 🎉)</p> <br>
<p>You will get test result in your output, also you can check test output in console and output folder.</p>

<h2>Dummy Input</h2>

``` bash
{
 "tests":[
    {
    "title":"Open google.com",
        "steps":[
            "Open Browser    http://www.google.com    chrome",
            "Go To    https://shyam-sunder.onrender.com/"
        ]
    },
    {
        "title":"visit about me page",
        "steps":[
            "Press Keys    id=about-me   \\13"
        ]
    },
    {
        "title":"Test valid login to Swag Labs",
        "steps":[
            "Open Browser    http://www.google.com    chrome",
            "Go To    https://www.saucedemo.com/",
            "Input Text    id=user-name    standard_user",
            "Input Text    id=password    secret_sauce",
            "Click Button   id=login-button",
            "Page Should Contain    Products"
        ]
    },
    {
        "title":"Test invalid username login to Swag Labs",
        "steps":[
            "Open Browser    http://www.google.com    chrome",
            "Go To    https://www.saucedemo.com/",
            "Input Text    id=user-name    invalidUser",
            "Input Text    id=password    secret_sauce",
            "Click Button   id=login-button",
            "Page Should Contain    Epic sadface: Username and password do not match any user in this service"
        ]
    },
    {
        "title":"check add button functionality",
        "steps":[
            "Open Browser    http://www.google.com    chrome",
            "Go To    https://the-internet.herokuapp.com/add_remove_elements/",
            "Click Button   Add Element",
            "Page Should Contain    Delete"
        ]
    },
    {
        "title":"Check forget password functionality for OrangeHRM website",
        "steps":[
            "Open Browser    http://www.google.com    chrome",
            "Go To    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
            "Click Element   class=orangehrm-login-forgot-header",
            "Page Should Contain    Reset Password",
            "Input Text    name=username    Admin",
            "Click Button    Reset Password",
            "Page Should Contain    Reset Password link sent successfully"
        ]
    }
 ]
}
```

<h2>Output for above code:</h2>

``` bash
{
    "status": "failure",
    "message": "Tests execution failed",
    "results": {
        "test_cases": [
            {
                "name": "Open google.com",
                "status": "PASS",
                "logs": "Open Browser\nOpening browser 'chrome' to base url 'http://www.google.com'.\nGo To\nOpening url 'https://shyam-sunder.onrender.com/'\n"
            },
            {
                "name": "visit about me page",
                "status": "PASS",
                "logs": "Press Keys\nSending key(s) ('13',) to id=about-me element.\nSending keys 13\n"
            },
            {
                "name": "Test valid login to Swag Labs",
                "status": "PASS",
                "logs": "Open Browser\nOpening browser 'chrome' to base url 'http://www.google.com'.\nGo To\nOpening url 'https://www.saucedemo.com/'\nInput Text\nTyping text 'standard_user' into text field 'id=user-name'.\nInput Text\nTyping text 'secret_sauce' into text field 'id=password'.\nClick Button\nClicking button 'id=login-button'.\nPage Should Contain\nCurrent page contains text 'Products'.\n"
            },
            {
                "name": "Test invalid username login to Swag Labs",
                "status": "PASS",
                "logs": "Open Browser\nOpening browser 'chrome' to base url 'http://www.google.com'.\nGo To\nOpening url 'https://www.saucedemo.com/'\nInput Text\nTyping text 'invalidUser' into text field 'id=user-name'.\nInput Text\nTyping text 'secret_sauce' into text field 'id=password'.\nClick Button\nClicking button 'id=login-button'.\nPage Should Contain\nCurrent page contains text 'Epic sadface: Username and password do not match any user in this service'.\n"
            },
            {
                "name": "check add button functionality",
                "status": "PASS",
                "logs": "Open Browser\nOpening browser 'chrome' to base url 'http://www.google.com'.\nGo To\nOpening url 'https://the-internet.herokuapp.com/add_remove_elements/'\nClick Button\nClicking button 'Add Element'.\nPage Should Contain\nCurrent page contains text 'Delete'.\n"
            },
            {
                "name": "Check forget password functionality for OrangeHRM website",
                "status": "FAIL",
                "logs": "Open Browser\nOpening browser 'chrome' to base url 'http://www.google.com'.\nGo To\nOpening url 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'\nClick Element\nClicking element 'class=orangehrm-login-forgot-header'.\n</td></tr><tr><td colspan=\"3\"><a href=\"selenium-screenshot-1.png\"><img src=\"selenium-screenshot-1.png\" width=\"800px\"></a>\nElement with locator 'class=orangehrm-login-forgot-header' not found.\nPage Should Contain\nInput Text\nClick Button\nPage Should Contain\n"
            }
        ]
    },
    "timestamp": "2024-04-10T04:08:36.371996",
    "start_time": "2024-04-10T04:08:36.371428",
    "end_time": "2024-04-10T04:08:36.371992",
    "time_taken": "0:00:00.000564"
}
```
