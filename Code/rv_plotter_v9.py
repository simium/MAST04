import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load the data
data = np.loadtxt('AG1_datos_1.txt', comments='#')
time, rv, error, phase = data[:, 0], data[:, 1], data[:, 2], data[:, 3]

# Known orbital period (days)
P = 2.6439

# Define the sinusoidal RV model
def rv_model(t, gamma, K, T0):
    return gamma + K * np.sin(2 * np.pi * (t - T0) / P)

# Initial guesses: gamma, K, T0
initial_guess = [np.mean(rv), (np.max(rv) - np.min(rv)) / 2, time[np.argmin(rv)]]

# Fit the model
popt, pcov = curve_fit(rv_model, time, rv, sigma=error, p0=initial_guess)
gamma_fit, K_fit, T0_fit = popt

# Print fit results
print(f"Systemic velocity γ = {gamma_fit:.2f} m/s")
print(f"Semi-amplitude K   = {K_fit:.2f} m/s")
print(f"Periastron time T₀  = {T0_fit:.5f} days")

# Generate smooth curve for plotting
t_smooth = np.linspace(min(time), max(time), 1000)
rv_fit_time = rv_model(t_smooth, *popt)

# Also generate fit vs phase
phase_smooth = (t_smooth - T0_fit) / P % 1
rv_fit_phase = rv_model(t_smooth, *popt)

# Plot: RV vs Time
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.errorbar(time, rv, yerr=error, fmt='o', capsize=3, color='gray', label='RV data')
plt.plot(t_smooth, rv_fit_time, color='darkred', label='Sine fit')
plt.xlabel('Time (days)')
plt.ylabel('Radial Velocity (m/s)')
plt.title('RV vs. Time')
plt.grid(True)
plt.legend()

# Plot: RV vs Phase
plt.subplot(1, 2, 2)
plt.errorbar(phase, rv, yerr=error, fmt='o', capsize=3, color='gray', label='RV data')
plt.plot(phase_smooth, rv_fit_phase, color='navy', label='Sine fit')
plt.xlabel('Orbital Phase')
plt.title('RV vs. Phase')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
