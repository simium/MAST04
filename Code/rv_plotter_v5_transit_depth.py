import numpy as np

# Load the data
data = np.loadtxt('AG1_datos_2.txt', comments='#')
hjd, flux, noise = data[:, 0], data[:, 1], data[:, 2]

# Optional: smooth flux to help with noise
from scipy.signal import savgol_filter
smoothed_flux = savgol_filter(flux, window_length=11, polyorder=3)

# Estimate baseline flux (outside transit): use top 20% highest points
baseline_flux = np.mean(np.sort(smoothed_flux)[-int(0.2 * len(smoothed_flux)):])

# Estimate min flux (during transit)
min_flux = np.min(smoothed_flux)

# Compute depth
transit_depth = baseline_flux - min_flux
percent_depth = transit_depth * 100  # Convert to %

print(f"Estimated transit depth: {transit_depth:.5f} (≈ {percent_depth:.2f}%)")
