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

def handle_missing_data(data, method='forward_fill'):
    """
    Handle missing data in the DataFrame.
    :param method: 'drop' to drop missing values, 'forward_fill', 'backward_fill', 'average'.
    """
    if method == 'drop':
        return data.dropna()
    elif method == 'forward_fill':
        data['value'] = data['value'].ffill()
    elif method == 'backward_fill':
        data['value'] = data['value'].bfill()
    elif method == 'average':
        avg_value = data['value'].astype(float).mean()
        data['value'] = data['value'].fillna(avg_value)
    else:
        raise ValueError("Method must be either 'drop', 'forward_fill', 'backward_fill', or 'average'.")
    return data

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

def process_emission_data(data, missing_data_method='forward_fill'):
    """Process the emission data."""
    df = pd.DataFrame(data['message'])
    inspect_data(df)
    df_sorted = sort_data(df, 'timestamp')
    check_missing_data(df_sorted)
    
    # Ensure 'value' column is of type float to correctly recognize NaNs
    df_sorted['value'] = pd.to_numeric(df_sorted['value'], errors='coerce')
    
    check_missing_data(df_sorted)  # Check missing data again after conversion
    df_cleaned = handle_missing_data(df_sorted, method=missing_data_method)
    expected_columns = ['timestamp', 'value', 'timestamp_readable']
    if check_file_format(df_cleaned, expected_columns):
        df_cleaned = df_cleaned[expected_columns]
    
    # Print date range for debugging
    print(f"Data timestamp range: {df_cleaned['timestamp'].min()} to {df_cleaned['timestamp'].max()}")
    
    return df_cleaned
