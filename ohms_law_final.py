# ---------------------------------------------------
# Lab 1: Ohm's Law Using Python
# Author: Micah Kipkurui
# Course: Fundamentals of Computer
#
# Objective:
# To apply Ohm’s Law using Python by calculating
# electric current and electrical power for
# different voltage and resistance values.
# ---------------------------------------------------

print("LAB 1: OHM'S LAW AND POWER SIMULATION\n")

# Experimental data (Voltage in volts, Resistance in ohms)
experimental_data = [
    {"Voltage": 5,  "Resistance": 10},
    {"Voltage": 10, "Resistance": 5},
    {"Voltage": 12, "Resistance": 6},
    {"Voltage": 9,  "Resistance": 3},
]

# Header for results table
print(f"{'Voltage (V)':<15}{'Resistance (Ω)':<18}{'Current (A)':<15}{'Power (W)':<12}")
print("-" * 60)

# Perform calculations and display results
for data in experimental_data:
    V = data["Voltage"]
    R = data["Resistance"]

    if R == 0:
        print(f"{V:<15}{R:<18}{'Error':<15}{'Error':<12}")
        continue

    I = V / R              # Ohm's Law: I = V / R
    P = V * I              # Power: P = V × I

    print(f"{V:<15}{R:<18}{I:<15.3f}{P:<12.3f}")

print("\nConclusion:")
print("The simulation confirms that current is directly proportional to voltage")
print("and inversely proportional to resistance, in agreement with Ohm’s Law.")
print("Power increases with both voltage and current as predicted by theory.")
