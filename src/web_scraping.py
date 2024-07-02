# src/web_scraping.py

import requests
from datetime import datetime

BASE_URL = "https://api.co2-monitor.org/"
API_KEY = ""

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

def get_expost_latest(region='DE'):
    """Fetch the latest historic emission factors for Germany."""
    endpoint = f"{BASE_URL}/public/expost_latest"
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Accept': 'application/json'
    }
    params = {
        'region': region
    }
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching expost latest data: {e}")
        return None

def get_co2_intensity(start_date, end_date, dataset='expost', scope='LC', region='DE'):
    """Fetch CO2 intensity data based on parameters."""
    endpoint = f"{BASE_URL}/private"
    headers = {
        'Authorization': f'Bearer {API_KEY}',
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
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching CO2 intensity data: {e}")
        return None
