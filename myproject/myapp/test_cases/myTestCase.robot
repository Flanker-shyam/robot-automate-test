*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Test Cases ***
Check forget password functionality for OrangeHRM website
    Open Browser    http://www.google.com    chrome
    Go To    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
    Wait Until Element Is Visible    css:h5.oxd-text.oxd-text--h5.orangehrm-login-title
    Click Element   class=orangehrm-login-forgot-header
    Wait Until Element Is Visible    css:h6.oxd-text.oxd-text--h6.orangehrm-forgot-password-title
    Page Should Contain    Reset Password
    Input Text    name=username    Admin
    Click Button    Reset Password
    Page Should Contain    Reset Password link sent successfully
