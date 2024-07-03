# src/emission_calculator.py
# Functions to calculate emissions based on the data.

def calculate_emissions(emission_data, load_data):
    """
    Calculate emissions based on emission data and load data.
    :param emission_data: DataFrame with emission data.
    :param load_data: DataFrame with load data.
    """
    # Ensure that both data sets are sorted by timestamp
    emission_data = emission_data.sort_values(by='timestamp')
    load_data = load_data.sort_values(by='timestamp')
    
    # Merge the two datasets on timestamp
    merged_data = pd.merge(emission_data, load_data, on='timestamp', suffixes=('_emission', '_load'))
    
    # Calculate the emissions by multiplying emission values by load values
    merged_data['calculated_emissions'] = merged_data['value_emission'] * merged_data['value_load']
    
    return merged_data