import unittest
import pandas as pd
from demographic_data_analyzer import analyze_demographics

class TestDemographicDataAnalyzer(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
            'native-country': ['India', 'India', 'USA', 'USA', 'India'],
            'salary': ['>50K', '<=50K', '>50K', '>50K', '<=50K'],
            'occupation': ['Engineer', 'Teacher', 'Doctor', 'Lawyer', 'Engineer'],
            'education': ['Bachelors', 'Masters', 'Doctorate', 'Bachelors', 'Bachelors'],
            'sex': ['Male', 'Female', 'Male', 'Male', 'Male'],
            'age': [25, 35, 45, 55, 30],
            'HoursPerWeek': [40, 30, 50, 60, 20]
        })
        self.data.to_csv('test_data.csv', index=False)  # Save to CSV for testing

    def test_analyze_demographics(self):
        results = analyze_demographics('test_data.csv')
        self.assertEqual(results['highest_earning_country'], 'USA')
        self.assertEqual(results['highest_earning_country_percentage'], 67.0)
        self.assertEqual(results['most_popular_occupation_in_india'], 'Engineer')

if __name__ == '__main__':
    unittest.main()
