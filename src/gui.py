# src/gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt

def open_file():
    file_path = filedialog.askopenfilename()
    return file_path

def display_results(results):
    fig, ax = plt.subplots()
    ax.plot(results['timestamp'], results['emissions'])
    plt.show()

def create_gui():
    root = tk.Tk()
    root.title('CO2mpaRE')

    tk.Button(root, text='Open File', command=open_file).pack()
    tk.Button(root, text='Calculate Emissions', command=lambda: calculate_and_display()).pack()

    root.mainloop()

def calculate_and_display():
    file_path = open_file()
    consumption_data = load_data(file_path)
    co2_data = get_co2_intensity('http://example.com')  # Replace with actual URL
    total_emissions, results = calculate_emissions(consumption_data, co2_data)
    display_results(results)
    messagebox.showinfo('Total Emissions', f'Total Emissions: {total_emissions} kg CO2')

if __name__ == "__main__":
    create_gui()
