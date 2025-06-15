import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt('AG1_datos_2.txt', comments='#')
hjd, flux, noise = data[:, 0], data[:, 1], data[:, 2]
hjd_offset = hjd - np.mean(hjd)

# Estimate baseline flux (robustly: top 20% of points)
baseline_flux = np.mean(np.sort(flux)[-int(0.2 * len(flux)):])

# Estimate minimum flux directly
min_flux = np.min(flux)

# Transit depth
transit_depth = baseline_flux - min_flux
percent_depth = transit_depth * 100

print(f"Estimated transit depth: {transit_depth:.5f} (≈ {percent_depth:.2f}%)")

# Plot
plt.figure(figsize=(10, 5))
plt.plot(hjd_offset, flux, color='red', label='Flux (raw)')
plt.axhline(baseline_flux, color='green', linestyle='--', label='Baseline Flux')
plt.axhline(min_flux, color='blue', linestyle='--', label='Min Flux (Transit)')
plt.fill_between(hjd_offset, baseline_flux, min_flux, 
                 where=(flux < baseline_flux), color='skyblue', alpha=0.3, label='Transit Depth')
plt.xlabel('Time (HJD - mean)')
plt.ylabel('Relative Flux')
plt.title('Transit Depth Estimation (No Smoothing)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
