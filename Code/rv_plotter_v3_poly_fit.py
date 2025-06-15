import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt('AG1_datos_2.txt', comments='#')
hjd, flux, noise = data[:, 0], data[:, 1], data[:, 2]

# Optional: shift time axis to center around zero for easier reading
hjd_offset = hjd - np.mean(hjd)

# Fit a low-degree polynomial (e.g., degree 5 or 7)
coeffs = np.polyfit(hjd_offset, flux, deg=5)
poly = np.poly1d(coeffs)

# Generate smooth curve
hjd_smooth = np.linspace(hjd_offset.min(), hjd_offset.max(), 1000)
flux_smooth = poly(hjd_smooth)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(hjd_offset, flux, color='lightgray', label='Original Flux')
plt.plot(hjd_smooth, flux_smooth, color='red', linewidth=2, label='Smoothed Flux (Poly Fit)')
plt.xlabel('Time (HJD - mean)')
plt.ylabel('Relative Flux')
plt.title('Polynomial-Fit Smoothed Transit Curve')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
