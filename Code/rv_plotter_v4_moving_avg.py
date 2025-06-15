import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt('AG1_datos_2.txt', comments='#')
hjd, flux, noise = data[:, 0], data[:, 1], data[:, 2]

# Optional: shift time axis to center around zero for easier reading
hjd_offset = hjd - np.mean(hjd)

def moving_average(y, window_size=5):
    return np.convolve(y, np.ones(window_size)/window_size, mode='valid')

# Smooth the flux
smoothed_flux = moving_average(flux, window_size=11)
smoothed_time = hjd_offset[(11 - 1)//2 : -(11 - 1)//2]  # Match length

# Plot
plt.figure(figsize=(10, 5))
plt.plot(hjd_offset, flux, color='lightgray', label='Original Flux')
plt.plot(smoothed_time, smoothed_flux, color='red', linewidth=2, label='Smoothed Flux (Moving Avg)')
plt.xlabel('Time (HJD - mean)')
plt.ylabel('Relative Flux')
plt.title('Smoothed Stellar Transit Curve')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
