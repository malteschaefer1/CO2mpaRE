# main.py
# For calling on individual files and functions

import sys
import os
from datetime import datetime

# Dynamically add the src directory to the system path
current_dir = os.path.dirname(__file__)
src_dir = os.path.join(current_dir, 'src')
sys.path.append(src_dir)

from web_scraping import get_emission_data, save_emission_data_to_sqlite
from data_processing import process_emission_data
from file_handling import save_to_csv

def main():
    # Ensure the data directory exists
    data_dir = os.path.join(current_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    start_date = "2023-09-01T00:00:00Z"
    end_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    # Fetch emission data
    print(f"Fetching emission data from {start_date} to {end_date}")
    emission_data = get_emission_data(start_date, end_date)
    if emission_data:
        print(f"Fetched {len(emission_data['message'])} data points")
        
        # Process the emission data
        processed_data = process_emission_data(emission_data)
        print(f"Processed data: {processed_data.head()}")
        
        # Save the processed data to SQLite
        sqlite_file_path = os.path.join(data_dir, 'emission_data.db')
        save_emission_data_to_sqlite(processed_data, sqlite_file_path)
        
        # Optionally, save the processed data to a CSV file
        csv_file_path = os.path.join(data_dir, 'emission_data.csv')
        save_to_csv(processed_data, csv_file_path)
        print(f"Data saved to {csv_file_path}")

if __name__ == "__main__":
    main()