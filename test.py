import pandas as pd

# Load the JSON file into a DataFrame
json_file = r'C:\Users\kunal.joshi\Downloads\Schedule_location_data_genrator.json'
df = pd.read_json(json_file)

# Convert the DataFrame to a CSV file
csv_file = r'C:\Users\kunal.joshi\Downloads\output.csv'
df.to_csv(csv_file, index=False)  # Set index to False to avoid writing the DataFrame index to the CSV

print(f'JSON file "{json_file}" has been converted to CSV file "{csv_file}".')
