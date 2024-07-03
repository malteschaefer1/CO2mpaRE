# tests/test_web_scraping.py
# For testing the web scraping functionality

import sys
import os
from datetime import datetime, timezone

# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from web_scraping import get_emission_data, save_emission_data_to_sqlite

def test_get_emission_data():
    """Test for fetching emission data."""
    start_date = "2023-09-01T00:00:00Z"
    end_date = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    try:
        emission_data = get_emission_data(start_date, end_date)
        assert emission_data is not None
        if 'message' in emission_data and emission_data['message']:
            # Ensure the data/test directory exists
            test_data_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'test')
            os.makedirs(test_data_dir, exist_ok=True)
            
            # Save the emission data to SQLite in the data/test directory
            sqlite_file_path = os.path.join(test_data_dir, 'test_emission_data.db')
            save_emission_data_to_sqlite(emission_data, sqlite_file_path)
            
            for entry in emission_data['message']:
                assert 'timestamp' in entry
                assert 'value' in entry
        else:
            assert False, "Emission data is empty."
    except Exception as e:
        assert False, f"Error fetching emission data: {e}"

if __name__ == "__main__":
    test_get_emission_data()
    print("All tests passed.")