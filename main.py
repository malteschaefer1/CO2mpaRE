# main.py
# For calling on individual files and functions

import sys
import os
from datetime import datetime

# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from web_scraping import get_emission_data, save_emission_data_to_sqlite
from data_processing import process_emission_data
from file_handling import save_to_csv

def main():
    # Ensure the data directory exists
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    start_date = "2023-09-01T00:00:00Z"
    end_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    # Fetch emission data
    emission_data = get_emission_data(start_date, end_date)
    if emission_data:
        # Process the emission data
        processed_data = process_emission_data(emission_data)
        
        # Save the processed data to SQLite
        sqlite_file_path = os.path.join(data_dir, 'emission_data.db')
        save_emission_data_to_sqlite(processed_data, sqlite_file_path)
        
        # Optionally, save the processed data to a CSV file
        csv_file_path = os.path.join(data_dir, 'emission_data.csv')
        save_to_csv(processed_data, csv_file_path)

if __name__ == "__main__":
    main()