import subprocess
import time
import os
from .constants import FILE_PATH, OUTPUT_DIR

def generate_robot_test_suite(test_data):
    """
    Generate a Robot Framework test suite based on the provided test data.

    Args:
        test_data (list): A list of dictionaries representing the test data. Each dictionary should have a "title" key
                          for the test title and a "steps" key for the test steps.

    Returns:
        str: The generated Robot Framework test suite as a string.
    """
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
    
def execute_robot_tests(robot_test_suite):
    """
    Executes the given Robot Framework test suite.

    Args:
        robot_test_suite (str): The Robot Framework test suite to be executed.

    Returns:
        str: The result of the test suite execution, or an error message if an exception occurs.
    """
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
    """
    Run the robot test suite using the provided test data.

    Args:
        test_data: The data used to generate the robot test suite.

    Returns:
        If an error occurs during test execution, the error message is returned.
        Otherwise, None is returned.
    """
    robot_test_suite = generate_robot_test_suite(test_data)
    
    error = execute_robot_tests(robot_test_suite)
    if error:
        return error
        
