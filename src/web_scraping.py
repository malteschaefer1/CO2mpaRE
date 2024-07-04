import requests
import csv
import os
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

def save_emission_data_to_csv(emission_data, csv_file_path):
    """Save emission data to a CSV file."""
    try:
        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ['timestamp', 'value', 'timestamp_readable']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader()
            for entry in emission_data['message']:
                writer.writerow({
                    'timestamp': entry['timestamp'],
                    'value': entry['value'],
                    'timestamp_readable': entry['timestamp_readable']
                })
        
        print(f"Data saved to {csv_file_path} successfully.")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")
