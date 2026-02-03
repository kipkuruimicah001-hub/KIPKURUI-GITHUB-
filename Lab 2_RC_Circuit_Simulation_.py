# Lab 2: RC Circuit Simulation
# Objective: Simulate the charging and discharging of a capacitor in an RC circuit

import numpy as np
import matplotlib.pyplot as plt

# Parameters
R = 1000       # Resistance in Ohms
C = 1e-6       # Capacitance in Farads
V = 5          # Supply voltage in Volts

# Time array: simulate up to 5 times the time constant
tau = R * C
t_max = 5 * tau
t = np.linspace(0, t_max, 1000)

# Capacitor charging: Vc(t) = V * (1 - exp(-t/RC))
Vc_charge = V * (1 - np.exp(-t / tau))

# Capacitor discharging: Vc(t) = V * exp(-t/RC)
Vc_discharge = V * np.exp(-t / tau)

# Plot charging and discharging curves
plt.figure(figsize=(8, 5))
plt.plot(t, Vc_charge, label='Charging (Vc = V(1 - exp(-t/RC)))', color='blue')
plt.plot(t, Vc_discharge, label='Discharging (Vc = V exp(-t/RC))', color='red')
plt.axhline(V, color='gray', linestyle='--', linewidth=1, label='Supply Voltage V')
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title(f"RC Circuit Charging & Discharging\nR={R} Ohms, C={C} F, Time Constant τ={tau:.6f} s")
plt.legend()
plt.grid(True)
plt.show()

# Observations
print(f"Time constant τ = R * C = {tau:.6f} seconds")
print("Observations:")
print("1. Charging curve starts at 0 V and approaches V asymptotically.")
print("2. Discharging curve starts at V and decays to 0 V exponentially.")
print("3. Increasing R or C increases τ, slowing voltage changes.")
print("4. Decreasing R or C decreases τ, speeding voltage changes.")
print("5. RC circuits are used in timers, filters, and signal processing.")
