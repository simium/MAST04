import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load the data
data = np.loadtxt('AG1_datos_1.txt', comments='#')
time, rv, error, phase = data[:, 0], data[:, 1], data[:, 2], data[:, 3]

# Known orbital period (days)
P = 2.6439

# Sinusoidal model for circular orbit
def rv_model_phase(phi, gamma, K, phi0):
    return gamma + K * np.sin(2 * np.pi * (phi - phi0))

# Initial guess: systemic velocity, semi-amplitude, phase offset
initial_guess = [np.mean(rv), (np.max(rv) - np.min(rv)) / 2, 0.0]

# Fit model to phase data
popt, pcov = curve_fit(rv_model_phase, phase, rv, sigma=error, p0=initial_guess)
gamma_fit, K_fit, phi0_fit = popt

# Print results
print(f"Fitted γ  = {gamma_fit:.2f} m/s")
print(f"Fitted K  = {K_fit:.2f} m/s")
print(f"Fitted φ₀ = {phi0_fit:.3f}")

# Generate smooth curve
phase_smooth = np.linspace(0, 1, 1000)
rv_fit = rv_model_phase(phase_smooth, *popt)

# Plot RV vs Phase with fit
plt.figure(figsize=(8, 4))
plt.errorbar(phase, rv, yerr=error, fmt='o', capsize=3, color='gray', label='RV data')
plt.plot(phase_smooth, rv_fit, color='darkblue', label='Sinusoidal fit')
plt.xlabel('Orbital Phase')
plt.ylabel('Radial Velocity (m/s)')
plt.title('RV vs. Phase with Trend Line')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
