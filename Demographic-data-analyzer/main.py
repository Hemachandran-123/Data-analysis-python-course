from demographic_data_analyzer import analyze_demographics

def main():
    results = analyze_demographics('C:\\Users\\HEMACHANDRAN M\\Downloads\\adult.data.csv')
    
    print("Race count:\n", results['race_count'])
    print("Average age of males:", results['average_age_of_males'])
    print("Percentage of Bachelors:", results['bachelor_percentage'])
    print("Percentage of people with advanced education earning >50K:", results['percentage_with_advanced_education'])
    print("Percentage of people without advanced education earning >50K:", results['percentage_without_advanced_education'])
    print("Minimum hours worked per week:", results['minimum_hours_worked'])
    print("Percentage of people working minimum hours earning >50K:", results['percentage_min_hours_high_income'])
    print(f"Country with the highest percentage of people earning >50K: {results['highest_earning_country']} ({results['highest_earning_country_percentage']}%)")
    print("Most popular occupation for those earning >50K in India:", results['most_popular_occupation_in_india'])

if __name__ == '__main__':
    main()
