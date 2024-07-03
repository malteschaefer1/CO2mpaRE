# src/web_scraping.py
# Code to download emission data from the API.

import requests
import sqlite3
from datetime import datetime
import config  # Assuming CO2_MONITOR_API_KEY is stored in config.py

BASE_URL = "https://api.co2-monitor.org/"
API_KEY = config.CO2_MONITOR_API_KEY

def check_api_health():
    """Check if the API is healthy."""
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        data = response.json()
        if 'message' in data:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error checking API health: {e}")
        return False

def get_emission_data(start_date, end_date, dataset='expost', scope='LC', region='DE'):
    """Fetch CO2 emission data based on parameters."""
    endpoint = f"{BASE_URL}/private"
    headers = {
        'x-api-key': API_KEY,
        'Accept': 'application/json'
    }
    params = {
        'from_ts': start_date,
        'to_ts': end_date,
        'region': region,
        'dataset': dataset,
        'scope': scope
    }
    try:
        print(f"Requesting {endpoint} with headers {headers} and params {params}")
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Print date range of fetched data for debugging
        if 'message' in data and data['message']:
            timestamps = [entry['timestamp'] for entry in data['message']]
            print(f"Fetched data timestamp range: {min(timestamps)} to {max(timestamps)}")
        
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response status code: {response.status_code}")
        print(f"Response details: {response.text}")  # Print the response content for debugging
    except Exception as e:
        print(f"Error fetching emission data: {e}")
    return None

def save_emission_data_to_sqlite(emission_data, db_file):
    """Save emission data to SQLite database."""
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS emission_data (
                timestamp INTEGER PRIMARY KEY,
                value REAL,
                timestamp_readable TEXT
            )
        ''')

        for entry in emission_data['message']:
            cursor.execute('''
                INSERT INTO emission_data (timestamp, value, timestamp_readable)
                VALUES (?, ?, ?)
            ''', (entry['timestamp'], entry['value'], entry['timestamp_readable']))

        conn.commit()
        print(f"Data saved to {db_file} successfully.")
    except Exception as e:
        print(f"Error saving data to SQLite: {e}")
    finally:
        if conn:
            conn.close()