import subprocess
import time
import os
from .constants import FILE_PATH, OUTPUT_DIR

def generate_robot_test_suite(test_data):
    robot_test_suite = ""
    robot_test_suite += f"*** Settings ***\n"
    robot_test_suite += f"Library    SeleniumLibrary\n"
    robot_test_suite += f"Library    OperatingSystem\n"
    robot_test_suite += f"Library    Collections\n\n"
    
    for test in test_data:
        test_title = test.get("title", "")
        test_steps = test.get("steps", [])
        
        robot_test_suite += f"*** Test Cases ***\n{test_title}\n"
        
        for step in test_steps:
            robot_test_suite += f"    {step}\n"
        
    return robot_test_suite


# def execute_robot_tests(robot_test_suite):
#     test_suite_file = "myapp/test_cases/myTestCase.robot"
    
#     try:
#         with open(test_suite_file, "w") as file:
#             file.write(robot_test_suite)
        
#         os.chmod(test_suite_file, 0o755)
        
#         time.sleep(5)

#         print("executing test suite ....", test_suite_file)
        
#         command = ["robot", "--outputdir", "myapp/output", test_suite_file]
        
#         subprocess.run(command)
#         print("Test suite execution completed.")
#     except Exception as e:
#         return str(e)
    
def execute_robot_tests(robot_test_suite):
    test_suite_file = FILE_PATH
    
    try:
        with open(test_suite_file, "w") as file:
            file.write(robot_test_suite)
        
        os.chmod(test_suite_file, 0o755)

        print("Executing test suite:", test_suite_file)

        command = ["pabot", "--processes", "2", "--outputdir", OUTPUT_DIR, test_suite_file]
        subprocess.run(command)
        
        print("Test suite execution completed.")
    except Exception as e:
        return str(e)

def run_test(test_data):
    robot_test_suite = generate_robot_test_suite(test_data)
    
    error = execute_robot_tests(robot_test_suite)
    if error:
        return error
        
