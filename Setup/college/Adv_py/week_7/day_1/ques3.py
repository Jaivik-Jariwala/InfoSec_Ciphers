import os
import json

# Function to read COVID-19 data from a JSON file
def read_covid_data(filepath):
    with open(filepath, "r") as json_file:
        data = json.load(json_file)
        return data

# Initialize dictionaries to store COVID-19 statistics
country_statistics = {}
all_countries = []

# Directory containing the JSON files
data_directory = "covid_data"

# Traverse the directory and its subdirectories to process JSON files
for root, _, files in os.walk(data_directory):
    for file in files:
        if file.endswith(".json"):
            filepath = os.path.join(root, file)
            covid_data = read_covid_data(filepath)
            
            # Extract relevant data
            country = covid_data["country"]
            total_confirmed = covid_data["confirmed_cases"]["total"]
            total_deaths = covid_data["deaths"]["total"]
            total_recovered = covid_data["recovered"]["total"]
            total_active = total_confirmed - total_deaths - total_recovered
            
            # Store statistics for each country
            country_statistics[country] = {
                "Total Confirmed Cases": total_confirmed,
                "Total Deaths": total_deaths,
                "Total Recovered Cases": total_recovered,
                "Total Active Cases": total_active
            }
            
            all_countries.append(country)

# Determine the top 5 countries with the highest and lowest confirmed cases
top_5_highest_confirmed = sorted(all_countries, key=lambda x: country_statistics[x]["Total Confirmed Cases"], reverse=True)[:5]
top_5_lowest_confirmed = sorted(all_countries, key=lambda x: country_statistics[x]["Total Confirmed Cases"])[:5]

# Generate a summary report in JSON format
summary_report = {
    "All Countries": country_statistics,
    "Top 5 Countries with Highest Confirmed Cases": top_5_highest_confirmed,
    "Top 5 Countries with Lowest Confirmed Cases": top_5_lowest_confirmed
}

# Save the summary report to a JSON file
with open("covid19_summary.json", "w") as json_file:
    json.dump(summary_report, json_file, indent=4)

print("COVID-19 summary report has been saved to 'covid19_summary.json'")
