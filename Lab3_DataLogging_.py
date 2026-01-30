# Lab 3: Data Logging and Visualization in Python

import random
import time
import matplotlib.pyplot as plt

# -----------------------
# Parameters
# -----------------------
num_samples = 10         # Number of readings
sampling_interval = 0.5  # Time between readings in seconds

# -----------------------
# Lists to store data
# -----------------------
temps = []       # Temperature values
humidity = []    # Humidity values
time_values = [] # Time values

# -----------------------
# File names
# -----------------------
csv_file_name = "environment_data.csv"
txt_file_name = "environment_data.txt"

# -----------------------
# Initialize files and start data logging
# -----------------------
try:
    with open(csv_file_name, "a") as csv_file, open(txt_file_name, "a") as txt_file:
        # Write headers
        csv_file.write("Time(s),Temperature(C),Humidity(%)\n")
        txt_file.write("Time(s)\tTemperature(C)\tHumidity(%)\n")
        
        print("Starting Data Logging...\n")
        print(f"{'Time(s)':>8} | {'Temp(C)':>8} | {'Hum(%)':>8}")
        print("-"*30)
        
        # -----------------------
        # Data sampling loop
        # -----------------------
        for t in range(num_samples):
            temp = 25 + random.uniform(-1, 1)  # Temperature ~25°C ±1
            hum = 50 + random.uniform(-5, 5)   # Humidity ~50% ±5

            temps.append(temp)
            humidity.append(hum)
            time_values.append(t)

            # Write data to files
            csv_file.write(f"{t},{temp:.2f},{hum:.2f}\n")
            txt_file.write(f"{t}\t{temp:.2f}\t{hum:.2f}\n")

            # Display in terminal
            print(f"{t:>8} | {temp:>8.2f} | {hum:>8.2f}")

            time.sleep(sampling_interval)

except IOError as e:
    print("File operation error:", e)

# -----------------------
# Calculations
# -----------------------
avg_temp = sum(temps) / len(temps)
avg_hum = sum(humidity) / len(humidity)
min_temp = min(temps)
max_temp = max(temps)
min_hum = min(humidity)
max_hum = max(humidity)

# Rate of change for temperature and humidity
rate_temp = [(temps[i+1]-temps[i])/sampling_interval for i in range(len(temps)-1)]
rate_hum = [(humidity[i+1]-humidity[i])/sampling_interval for i in range(len(humidity)-1)]

# -----------------------
# Print summary
# -----------------------
print("\n--- Summary ---")
print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Average Humidity: {avg_hum:.2f} %")
print(f"Temperature: min={min_temp:.2f} °C, max={max_temp:.2f} °C")
print(f"Humidity: min={min_hum:.2f} %, max={max_hum:.2f} %")
print(f"Temperature rate of change (°C/s): {rate_temp}")
print(f"Humidity rate of change (%/s): {rate_hum}")

# -----------------------
# Plotting
# -----------------------
plt.figure(figsize=(10,5))
plt.plot(time_values, temps, marker='o', linestyle='-', color='red', label="Temperature (°C)")
plt.plot(time_values, humidity, marker='s', linestyle='--', color='blue', label="Humidity (%)")
plt.xlabel("Time (s)")
plt.ylabel("Measured Values")
plt.title("Environmental Data Logging with Statistics")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
