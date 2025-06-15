import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt('AG1_datos_1.txt', comments='#')
time, rv, error, phase = data[:, 0], data[:, 1], data[:, 2], data[:, 3]

# Create figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 4), sharey=True)

# Plot 1: RV vs Time
axs[0].errorbar(time, rv, yerr=error, fmt='o', capsize=3, color='darkred')
axs[0].set_xlabel('Time (days)')
axs[0].set_ylabel('Radial Velocity (m/s)')
axs[0].set_title('RV vs. Time')
axs[0].grid(True)

# Plot 2: RV vs Phase
axs[1].errorbar(phase, rv, yerr=error, fmt='o', capsize=3, color='navy')
axs[1].set_xlabel('Orbital Phase')
axs[1].set_title('RV vs. Phase')
axs[1].grid(True)

# Layout
plt.tight_layout()
plt.show()
