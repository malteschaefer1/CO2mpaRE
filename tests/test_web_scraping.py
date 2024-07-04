# tests/test_web_scraping.py
# For testing the web scraping functionality

import sys
import os
from datetime import datetime, timezone
import csv

# Dynamically add the src directory to the system path
current_dir = os.path.dirname(__file__)
src_dir = os.path.join(current_dir, '..', 'src')
sys.path.append(src_dir)

from web_scraping import get_emission_data, save_emission_data_to_csv

def test_get_emission_data():
    """Test for fetching emission data."""
    start_date = "2024-06-01T00:00:00Z"
    end_date = "2024-06-15T23:00:00Z"

    try:
        emission_data = get_emission_data(start_date, end_date)
        assert emission_data is not None
        if 'message' in emission_data and emission_data['message']:
            # Ensure the data/test directory exists
            test_data_dir = os.path.join(current_dir, '..', 'data', 'test')
            os.makedirs(test_data_dir, exist_ok=True)
            
            # Save the emission data to CSV in the data/test directory
            csv_file_path = os.path.join(test_data_dir, 'test_emission_data.csv')
            save_emission_data_to_csv(emission_data, csv_file_path)
            
            # Verify the CSV file content
            with open(csv_file_path, mode='r') as csv_file:
                reader = csv.DictReader(csv_file)
                rows = list(reader)
                assert len(rows) == len(emission_data['message'])
                for row in rows:
                    assert 'timestamp' in row
                    assert 'value' in row
                    assert 'timestamp_readable' in row
        else:
            assert False, "Emission data is empty."
    except Exception as e:
        assert False, f"Error fetching emission data: {e}"

if __name__ == "__main__":
    test_get_emission_data()
    print("All tests passed.")
