import xml.etree.ElementTree as ET
from datetime import datetime

def parse_output_xml(xml_file):
    """
    Parses the given XML file and extracts test information.

    Args:
        xml_file (str): The path to the XML file.

    Returns:
        list: A list of dictionaries containing test information. Each dictionary has the following keys:
            - name (str): The name of the test.
            - status (str): The status of the test.
            - logs (str): The logs associated with the test.

        Returns None if an error occurs during parsing.
    """
    try:
        results = []
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for test in root.findall('.//test'):
            test_name = test.get('name')
            test_status = test.find('status').get('status')
            test_logs = ''
            for kw in test.findall('.//kw'):
                test_logs += kw.get('name') + '\n'
                for msg in kw.findall('.//msg'):
                    test_logs += msg.text + '\n'
            results.append({'name': test_name, 'status': test_status, 'logs': test_logs})

        return results
    except Exception as e:
        print(f"Error occurred while parsing {xml_file}: {e}")
        return None

def generate_result_summary(results, start_time, end_time):
    """
    Generate a summary of the test results.

    Args:
        results (list): A list of test results.
        start_time (datetime): The start time of the test execution.
        end_time (datetime): The end time of the test execution.

    Returns:
        dict: A dictionary containing the summary of the test results.
    """
    if results is None:
        return None

    passed_tests = [test for test in results if test['status'] == 'PASS']
    failed_tests = [test for test in results if test['status'] == 'FAIL']

    time_taken = end_time - start_time

    summary = {
        'status': 'success' if len(failed_tests) == 0 else 'failure',
        'message': 'Tests executed successfully' if len(failed_tests) == 0 else 'Tests execution failed',
        'results': {
            'test_cases': results
        },
        'timestamp': datetime.now().isoformat(),
        'start_time': start_time.isoformat(),
        'end_time': end_time.isoformat(),
        'time_taken': str(time_taken)
    }
    return summary

def handle_output(file_name):
    """
    Handles the output file by parsing it and generating a result summary.

    Args:
        file_name (str): The name of the output file to be parsed.

    Returns:
        str: The generated result summary if successful, None otherwise.
    """
    start_time = datetime.now()
    results = parse_output_xml(file_name)
    end_time = datetime.now()
    
    if results is not None:
        summary = generate_result_summary(results, start_time, end_time)
        if summary is not None:
            print(summary)
            return summary
        else:
            print("Failed to generate result summary.")
            return None
    else:
        print("Failed to parse output XML file.")
        return None
