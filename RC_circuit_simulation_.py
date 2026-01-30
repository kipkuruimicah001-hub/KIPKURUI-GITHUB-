"""
Lab 2: RC Circuit Simulation
Author: Micah Kipkurui
Description:
This program simulates the charging and discharging of a capacitor in a series RC circuit.
It calculates capacitor voltage over time, shows the effect of the time constant, and plots
the charging and discharging curves.
"""

# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# Circuit Parameters
# --------------------------
R = 1000       # Resistance in ohms
C = 1e-6       # Capacitance in farads
V = 5          # Supply voltage in volts

# Calculate the time constant
tau = R * C    # RC time constant in seconds
print(f"Time constant (tau) = {tau} seconds\n")

# --------------------------
# Time vector for simulation
# --------------------------
t = np.linspace(0, 5*tau, 1000)  # simulate for 5 time constants

# --------------------------
# Capacitor Voltage Calculations
# --------------------------
# Charging voltage over time: Vc = V * (1 - exp(-t/RC))
Vc_charge = V * (1 - np.exp(-t / (R * C)))

# Discharging voltage over time: Vc = V * exp(-t/RC)
Vc_discharge = V * np.exp(-t / (R * C))

# --------------------------
# Numeric examples at key points
# --------------------------
# Voltage after 1 time constant (t = tau)
Vc_charge_1tau = V * (1 - np.exp(-1))
Vc_discharge_1tau = V * np.exp(-1)
print(f"Voltage after 1 time constant (charging) = {Vc_charge_1tau:.3f} V")
print(f"Voltage after 1 time constant (discharging) = {Vc_discharge_1tau:.3f} V\n")

# Voltage after 5 time constants (t = 5*tau)
Vc_charge_5tau = V * (1 - np.exp(-5))
Vc_discharge_5tau = V * np.exp(-5)
print(f"Voltage after 5 time constants (charging) = {Vc_charge_5tau:.3f} V")
print(f"Voltage after 5 time constants (discharging) = {Vc_discharge_5tau:.3f} V\n")

# --------------------------
# Plotting the results
# --------------------------
plt.figure(figsize=(10,6))
plt.plot(t, Vc_charge, label='Charging', color='green', linewidth=2)
plt.plot(t, Vc_discharge, label='Discharging', color='red', linewidth=2)
plt.axvline(x=tau, color='blue', linestyle='--', label='1 Time Constant (tau)')
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Capacitor Voltage (V)', fontsize=12)
plt.title('RC Circuit: Capacitor Charging and Discharging', fontsize=14)
plt.legend()
plt.grid(True)
plt.show()
