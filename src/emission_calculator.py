# src/emission_calculator.py

def calculate_emissions(consumption_data, co2_data):
    merged_data = pd.merge(consumption_data, co2_data, on='timestamp')
    merged_data['emissions'] = merged_data['consumption'] * merged_data['co2_intensity']
    total_emissions = merged_data['emissions'].sum()
    return total_emissions, merged_data
