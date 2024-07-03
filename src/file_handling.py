# src/file_handling.py
# Functions to read from and write to files, including user-uploaded data.

import pandas as pd

def read_csv(file_path):
    """Read a CSV file and return a DataFrame."""
    return pd.read_csv(file_path)

def save_to_csv(data, file_path):
    """Save a DataFrame to a CSV file."""
    data.to_csv(file_path, index=False)