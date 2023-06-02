import csv
import os

# Get the current directory
current_directory = os.getcwd()

# List all files in the current directory
files = os.listdir(current_directory)

# Iterate over each file
for file_name in files:
    if file_name.endswith('.csv'):  # Check if the file is a CSV file
        file_path = os.path.join(current_directory, file_name)

        # Open the CSV file
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)

        # Check if the CSV file contains only one row
        if len(rows) == 1:
            # Delete the file
            os.remove(file_path)
            print(f"Deleted {file_name}")

