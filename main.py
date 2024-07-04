import sys
import os
from datetime import datetime
import pandas as pd

# Dynamically add the src directory to the system path
current_dir = os.path.dirname(__file__)
src_dir = os.path.join(current_dir, 'src')
sys.path.append(src_dir)

from web_scraping import get_emission_data, save_emission_data_to_csv
from data_processing import process_emission_data

def main():
    # Ensure the data directory exists
    data_dir = os.path.join(current_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    start_date = "2024-06-01T00:00:00Z"
    end_date = "2024-06-15T23:00:00Z"
    # datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    # Fetch emission data
    print(f"Fetching emission data from {start_date} to {end_date}")
    emission_data = get_emission_data(start_date, end_date)
    if emission_data:
        print(f"Fetched {len(emission_data['message'])} data points")
        
        # Process the emission data
        missing_data_method = 'forward_fill'  # Options: 'drop', 'forward_fill', 'backward_fill', 'average'
        processed_data = process_emission_data(emission_data, missing_data_method)
        print(f"Processed data: {processed_data.head()}")
        
        # Save the processed data to a CSV file
        csv_file_path = os.path.join(data_dir, 'emission_data.csv')
        save_emission_data_to_csv({'message': processed_data.to_dict('records')}, csv_file_path)
        print(f"Data saved to {csv_file_path}")

if __name__ == "__main__":
    main()
