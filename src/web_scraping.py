# src/web_scraping.py

import requests
import config  # Import your configuration module

BASE_URLS = {
    'co2_monitor': "https://api.co2-monitor.org/",
    # Add more base URLs for other services as needed
}

def co2_monitor_api_request(action, **kwargs):
    """Superior function to handle CO2 Monitor API requests."""
    api_key = config.CO2_MONITOR_API_KEY  # Access API key from config module
    if not api_key:
        raise ValueError("API key not found in configuration.")

    base_url = BASE_URLS.get('co2_monitor')
    if action == 'api_health':
        return check_api_health(base_url)
    elif action == 'get_expost_latest':
        region = kwargs.get('region', 'DE')
        return get_expost_latest(base_url, api_key, region=region)
    else:
        raise ValueError(f"Unsupported action: {action}")

def check_api_health(base_url):
    """Check if the CO2 Monitor API is healthy."""
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()
        if 'message' in data:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error checking CO2 Monitor API health: {e}")
        return False

def get_expost_latest(base_url, api_key, region='DE'):
    """Fetch the latest historic emission factors for Germany from CO2 Monitor."""
    endpoint = f"{base_url}/public/expost_latest"
    headers = {
        'Authorization': f'Bearer {api_key}',
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
        print(f"Error fetching expost latest data from CO2 Monitor: {e}")
        return None