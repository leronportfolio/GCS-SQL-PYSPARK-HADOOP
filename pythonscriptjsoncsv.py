import pandas as pd
import os

# Set the path to the Yelp academic dataset user JSON file
json_file_path = 'C:/Users/14089/Documents/yelp_academic_dataset_user.json'

# Read the JSON file into a Pandas DataFrame
df = pd.read_json(json_file_path, lines=True)

# Set the path for the output CSV/json file
csv_file_path = os.path.expanduser('~/Documents/yelp_academic_dataset_user.csv')

json_file_path = os.path.expanduser('~/Documents/yelp_academic_dataset_user.json')

# Save as a CSV file
df.to_csv(csv_file_path, index=False)

# Save as a JSON file
df.to_json(json_file_path, orient='records', lines=True)
