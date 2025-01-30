import json
import requests  
import pandas as pd

# Store the URL
url = "https://data.cityofnewyork.us/resource/hq68-rnsi.json?$offset=1000&$limit=10000"

# Send a GET request
response = requests.get(url)

# Parse JSON response
nyc_data_json = response.json()

# Save the data to a file (correct path and mode for writing)
with open("nyc_data.json", "w") as file:
    json.dump(nyc_data_json, file, indent=4)  # Save the JSON data

print("JSON data saved as nyc_data.json!")

# Convert the JSON data into a DataFrame
df = pd.DataFrame(nyc_data_json)

# Save the DataFrame to a CSV file
df.to_csv("nyc_data.csv", index=False)

print("CSV file saved as nyc_data.csv!")