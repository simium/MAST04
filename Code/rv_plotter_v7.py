import numpy as np
import matplotlib.pyplot as plt

# Load the data
# Adjust the filename as needed
data = np.loadtxt('AG1_datos_1.txt', comments='#')
time, rv, error, phase = data[:, 0], data[:, 1], data[:, 2], data[:, 3]

# Plot 1: RV vs Time
plt.figure(figsize=(10, 4))
plt.errorbar(time, rv, yerr=error, fmt='o', capsize=3, label='RV Data', color='darkred')
plt.xlabel('Time (days)')
plt.ylabel('Radial Velocity (m/s)')
plt.title('Radial Velocity vs. Time')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot 2: RV vs Phase
plt.figure(figsize=(10, 4))
plt.errorbar(phase, rv, yerr=error, fmt='o', capsize=3, label='RV by Phase', color='navy')
plt.xlabel('Orbital Phase')
plt.ylabel('Radial Velocity (m/s)')
plt.title('Radial Velocity Curve (Folded by Phase)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
