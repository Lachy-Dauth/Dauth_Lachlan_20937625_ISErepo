import sys
from io import StringIO
import temperature
import season_finder

def test_temperature_finder():
    test_cases = [
        {  
            'input': [18.0, "perth", "morning"],
            'expected_output': "It is colder than the mean temperature."
        },
        {  
            'input': [24.0, "perth", "afternoon"],
            'expected_output': "It is hotter than the mean temperature."
        },
        {  
            'input': [16, "adelaide", "morning"],
            'expected_output': "It is colder than the mean temperature."
        },
        {  
            'input': [23, "adelaide", "afternoon"],
            'expected_output': "It is hotter than the mean temperature."
        },
        {  
            'input': [18.2, "perth", "morning"],
            'expected_output': "It is the same as the mean temperature."
        },
        {  
            'input': [18, "perth", "afternoon"],
            'expected_output': "It is colder than the mean temperature."
        },
        {  
            'input': [28, "perth", "afternoon"],
            'expected_output': "It is hotter than the mean temperature."
        },
        {  
            'input': [17.9, "perth", "afternoon"],
            'expected_output': "It is 17.9 degrees outside, 5.1 degrees colder than the mean temperature, 23."
        },
        {  
            'input': [28.1, "perth", "afternoon"],
            'expected_output': "It is 28.1 degrees outside, 5.1 degrees hotter than the mean temperature, 23."
        }
        # Add more test cases for temperature_finder function here
    ]

    for i, test_case in enumerate(test_cases):
        # Capture the console output
        sys.stdout = StringIO()

        # Call the function
        temperature.temperature_finder(*test_case['input'])

        # Get the captured output
        actual_output = sys.stdout.getvalue().strip()

        # Reset sys.stdin and sys.stdout
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Check the output
        if actual_output == test_case['expected_output']:
            print(f"Test {i + 1}: Passed")
        else:
            print(f"Test {i + 1}: Failed")
            print("Expected Output:", test_case['expected_output'])
            print("Actual Output:", actual_output)

def test_month_to_season():
    test_cases = [
        {
            'input': ["January", "Australia"],
            'expected_output': "When it is January in Australia, it is the Summer season."
        },
        {
            'input': ["March", "Noongar"],
            'expected_output': "When it is March in Noongar, it is the Bunuru season."
        },
        {
            'input': ["July", "Spain"],
            'expected_output': "When it is July in Spain, it is the Summer season."
        },
        {
            'input': ["December", "Japan"],
            'expected_output': "When it is December in Japan, it is the Winter season."
        },
        {
            'input': ["May", "Mauritius"],
            'expected_output': "When it is May in Mauritius, it is the Autumn season."
        },
        {
            'input': ["September", "Sri Lanka"],
            'expected_output': "When it is September in Sri Lanka, it is the Southeast Monsoon season."
        },
        {
            'input': ["October", "Malaysia"],
            'expected_output': "When it is October in Malaysia, it is the Inter-Monsoon season."
        }
        # Add more test cases for month_to_season function here
    ]

    for i, test_case in enumerate(test_cases):
        # Capture the console output
        sys.stdout = StringIO()

        # Call the function
        season_finder.month_to_season(*test_case['input'])

        # Get the captured output
        actual_output = sys.stdout.getvalue().strip()

        # Reset sys.stdin and sys.stdout
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Check the output
        if actual_output == test_case['expected_output']:
            print(f"Test {i + 1}: Passed")
        else:
            print(f"Test {i + 1}: Failed")
            print("Expected Output:", test_case['expected_output'])
            print("Actual Output:", actual_output)

if __name__ == '__main__':
    print("Testing temperature_finder:")
    test_temperature_finder()

    print("\nTesting month_to_season:")
    test_month_to_season()
