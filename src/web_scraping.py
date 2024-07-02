# src/web_scraping.py

import requests
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt

def get_co2_intensity(start_date, end_date, dataset='expost', scope='2', region='DE'):
    # Base URL of the CO2 Monitor API
    base_url = "https://co2-monitor.org/api/private"
    
    # Your API key
    api_key = "w0lPQjP05y1W5wOz0TsIj9f3zxHr9qt18rN8Cfqc"
    
    # Headers for the request
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    
    # Parameters for the request
    params = {
        'from_ts': start_date,
        'to_ts': end_date,
        'region': region,
        'dataset': dataset,
        'scope': scope
    }
    
    # Make the request
    response = requests.get(base_url, headers=headers, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrieve data: {response.status_code}, {response.text}")
        return None

