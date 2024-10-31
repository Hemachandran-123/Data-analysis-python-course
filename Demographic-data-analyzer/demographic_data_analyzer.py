import pandas as pd
def load_data(file_path):
    return pd.read_csv(file_path)

def race_count(data):
    return data['race'].value_counts()

def average_age_of_males(data):
    return data[data['sex'] == 'Male']['age'].mean()

def bachelor_percentage(data):
    total_edu = data['education'].count()
    bach_count = data[data['education'] == 'Bachelors'].shape[0]
    return (bach_count / total_edu) * 100

def percentage_with_advanced_education(data):
    return (
        data[(data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (data['salary'] == '>50K')].shape[0] 
        / data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0]
    ) * 100

def percentage_without_advanced_education(data):
    return (
        data[(~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (data['salary'] == '>50K')].shape[0] 
        / data[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0]
    ) * 100

def minimum_hours_worked(data):
    return data['HoursPerWeek'].min()

def percentage_min_hours_high_income(data):
    min_hours = minimum_hours_worked(data)
    return (
        data[(data['HoursPerWeek'] == min_hours) & (data['salary'] == '>50K')].shape[0] 
        / data[data['HoursPerWeek'] == min_hours].shape[0]
    ) * 100

def highest_earning_country(data):
    country_percentage = (data[data['salary'] == '>50K']['native-country'].value_counts() /
                          data['native-country'].value_counts()) * 100
    highest_country = country_percentage.idxmax()
    highest_percentage = round(country_percentage.max(), 1)
    return highest_country, highest_percentage

def most_popular_occupation_in_india(data):
    return data[data['native-country'] == 'India']['occupation'].value_counts().idxmax()
