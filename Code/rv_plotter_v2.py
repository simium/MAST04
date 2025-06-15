import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt('AG1_datos_2.txt', comments='#')
hjd, flux, noise = data[:, 0], data[:, 1], data[:, 2]

# Optional: shift time axis to center around zero for easier reading
hjd_offset = hjd - np.mean(hjd)

# Compute upper and lower bounds for error band
flux_upper = flux + noise
flux_lower = flux - noise

# Create plot
plt.figure(figsize=(10, 5))

# Plot main light curve (red line)
plt.plot(hjd_offset, flux, color='red', label='Flux')

# Plot error band (blue lines)
plt.plot(hjd_offset, flux_upper, color='blue', linestyle='--', label='Flux + Noise')
plt.plot(hjd_offset, flux_lower, color='blue', linestyle='--', label='Flux - Noise')

# Customize plot
plt.xlabel('Time (HJD - mean)')
plt.ylabel('Relative Flux')
plt.title('Stellar Transit Light Curve with Error Bounds')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show plot
plt.show()
