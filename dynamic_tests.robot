*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open google.com
    Open Browser    http://www.google.com    chrome
    Go To    https://shyam-sunder.onrender.com/

visit about me page
    Press Keys    id=about-me   \\13
    Capture Page Screenshot
