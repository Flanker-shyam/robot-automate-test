*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Test Cases ***
Open google.com
    Open Browser    http://www.google.com    chrome
    Go To    https://shyam-sunder.onrender.com/
*** Test Cases ***
visit about me page
    Press Keys    id=about-me   \13
*** Test Cases ***
Test valid login to Swag Labs
    Open Browser    http://www.google.com    chrome
    Go To    https://www.saucedemo.com/
    Input Text    id=user-name    standard_user
    Input Text    id=password    secret_sauce
    Click Button   id=login-button
    Page Should Contain    Products
*** Test Cases ***
Test invalid username login to Swag Labs
    Open Browser    http://www.google.com    chrome
    Go To    https://www.saucedemo.com/
    Input Text    id=user-name    invalidUser
    Input Text    id=password    secret_sauce
    Click Button   id=login-button
    Page Should Contain    Epic sadface: Username and password do not match any user in this service
*** Test Cases ***
check add button functionality
    Open Browser    http://www.google.com    chrome
    Go To    https://the-internet.herokuapp.com/add_remove_elements/
    Click Button   Add Element
    Page Should Contain    Delete
*** Test Cases ***
Check forget password functionality for OrangeHRM website
    Open Browser    http://www.google.com    chrome
    Go To    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
    Click Element   class=orangehrm-login-forgot-header
    Page Should Contain    Reset Password
    Input Text    name=username    Admin
    Click Button    Reset Password
    Page Should Contain    Reset Password link sent successfully
