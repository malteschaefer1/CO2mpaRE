# src/data_processing.py
# Handle data processing tasks such as sorting, checking for missing data, and handling incorrect data.

import pandas as pd

def inspect_data(data):
    """Inspect the data, print its structure, and some basic statistics."""
    print(data.info())
    print(data.describe())
    print(data.head())

def sort_data(data, column):
    """Sort the data by a specific column."""
    return data.sort_values(by=column)

def check_missing_data(data):
    """Check for missing data and print the result."""
    missing_data = data.isnull().sum()
    print(f"Missing data in each column:\n{missing_data}")
    return missing_data

def handle_missing_data(data, method='drop', fill_value=None):
    """
    Handle missing data in the DataFrame.
    :param method: 'drop' to drop missing values, 'fill' to fill missing values.
    :param fill_value: Value to fill missing data if method is 'fill'.
    """
    if method == 'drop':
        return data.dropna()
    elif method == 'fill':
        return data.fillna(fill_value)
    else:
        raise ValueError("Method must be either 'drop' or 'fill'.")

def check_file_format(data, expected_columns):
    """Check if the data has the expected format (columns)."""
    actual_columns = list(data.columns)
    if set(expected_columns).issubset(set(actual_columns)):
        print("Data format is correct.")
        return True
    else:
        print(f"Expected columns: {expected_columns}")
        print(f"Actual columns: {actual_columns}")
        return False

def process_emission_data(data):
    """Process the emission data."""
    df = pd.DataFrame(data['message'])
    inspect_data(df)
    df_sorted = sort_data(df, 'timestamp')
    check_missing_data(df_sorted)
    df_cleaned = handle_missing_data(df_sorted)
    expected_columns = ['timestamp', 'value', 'timestamp_readable']
    if check_file_format(df_cleaned, expected_columns):
        df_cleaned = df_cleaned[expected_columns]
    
    # Print date range for debugging
    print(f"Data timestamp range: {df_cleaned['timestamp'].min()} to {df_cleaned['timestamp'].max()}")
    
    return df_cleaned