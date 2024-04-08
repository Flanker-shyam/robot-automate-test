import xml.etree.ElementTree as ET
from datetime import datetime

def parse_output_xml(xml_file):
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
