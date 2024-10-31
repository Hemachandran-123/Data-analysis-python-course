import pandas as pd

def analyze_demographics(file_path):
    data = pd.read_csv(file_path)
    results = {}
    
    results['race_count'] = data['race'].value_counts()
    
    results['average_age_of_males'] = data[data['sex'] == 'Male']['age'].mean()
    
    total_edu = data['education'].count()
    
    bach_count = data[data['education'] == 'Bachelors'].shape[0]
    results['bachelor_percentage'] = (bach_count / total_edu) * 100
    
    results['percentage_with_advanced_education'] = (
        data[(data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (data['salary'] == '>50K')].shape[0] 
        / data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0]
    ) * 100
    
    results['percentage_without_advanced_education'] = (
        data[(~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (data['salary'] == '>50K')].shape[0] 
        / data[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0]
    ) * 100
    
    results['minimum_hours_worked'] = data['HoursPerWeek'].min()
    
    min_hours = results['minimum_hours_worked']
    results['percentage_min_hours_high_income'] = (
        data[(data['HoursPerWeek'] == min_hours) & (data['salary'] == '>50K')].shape[0] 
        / data[data['HoursPerWeek'] == min_hours].shape[0]
    ) * 100
    
    country_percentage = (data[data['salary'] == '>50K']['native-country'].value_counts() /
                          data['native-country'].value_counts()) * 100
    results['highest_earning_country'] = country_percentage.idxmax()
    results['highest_earning_country_percentage'] = round(country_percentage.max(), 1)
    
    results['most_popular_occupation_in_india'] = data[data['native-country'] == 'India']['occupation'].value_counts().idxmax()
    
    return results
