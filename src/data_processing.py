# src/data_processing.py

def process_co2_data(data):
    # Assuming the data is in the 'message' field and is a list of dictionaries
    if 'message' in data:
        df = pd.DataFrame(data['message'])
        return df
    else:
        print("No data found in the response")
        return pd.DataFrame()

def display_results(df):
    if not df.empty:
        # Simple display of the first few rows
        print(df.head())
        
        # Plotting the data
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        plt.figure(figsize=(10, 5))
        plt.plot(df['timestamp'], df['value'], label='CO2 Intensity')
        plt.xlabel('Time')
        plt.ylabel('CO2 Intensity (gCO2/kWh)')
        plt.title('CO2 Intensity Over Time')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("No data to display")
