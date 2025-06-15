import numpy as np
import matplotlib.pyplot as plt

# Load the data from the text file
# Adjust delimiter if necessary (e.g., use ',' or '\t')
data = np.loadtxt('AG1_datos_2.txt', comments='#')

# Unpack the columns
hjd, flux, noise = data[:, 0], data[:, 1], data[:, 2]

# Optional: subtract mean HJD to make the x-axis easier to read
hjd_offset = hjd - np.mean(hjd)

# Plot the light curve with error bars
plt.figure(figsize=(10, 5))
plt.errorbar(hjd_offset, flux, yerr=noise, fmt='o', markersize=4, 
             ecolor='gray', capsize=2, label='Flux with Noise')

# Customize the plot
plt.xlabel('Time (HJD - mean)')
plt.ylabel('Relative Flux')
plt.title('Stellar Transit Light Curve')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()