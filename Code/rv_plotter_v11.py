import numpy as np

# Given values
K = 17.5          # m/s
P = 2.6439        # days
Ms = 0.45         # solar masses
Ms_max = 0.45 * 1.1  # maximum stellar mass (10% more)
Ms_min = 0.45 * 0.9  # minimum stellar mass (10% less)
e = 0.16          # eccentricity

# Mass formula (in Jupiter masses)
Mp_sini_mjup = 4.92e-3 * np.sqrt(1 - e**2) * K * P**(1/3) * Ms**(2/3)
# Calculate Mp sin(i) for maximum and minimum stellar mass
Mp_sini_mjup_max = 4.92e-3 * np.sqrt(1 - e**2) * K * P**(1/3) * Ms_max**(2/3)
Mp_sini_mjup_min = 4.92e-3 * np.sqrt(1 - e**2) * K * P**(1/3) * Ms_min**(2/3)
# calculate percentage of error in Mp sin(i) vs max and min
Mp_sini_mjup_error = (np.abs(Mp_sini_mjup_max - Mp_sini_mjup_min) / Mp_sini_mjup) * 100
Mp_sini_mjup_max_error = ((Mp_sini_mjup_max - Mp_sini_mjup)/ Mp_sini_mjup) * 100

# Convert to Earth masses
Mp_sini_mearth = Mp_sini_mjup * 317.8
# Convert maximum and minimum to Earth masses
Mp_sini_mearth_max = Mp_sini_mjup_max * 317.8
Mp_sini_mearth_min = Mp_sini_mjup_min * 317.8
# calculate error in Mp sin(i) vs max and min in Earth masses
Mp_sini_mearth_error = (np.abs(Mp_sini_mearth_max - Mp_sini_mearth_min) / Mp_sini_mearth) * 100

# Output
print(f"M_p sin(i) ≈ {Mp_sini_mjup:.5f} M_Jupiter")
print(f"Maximum M_p sin(i) ≈ {Mp_sini_mjup_max:.5f} M_Jupiter")
print(f"Minimum M_p sin(i) ≈ {Mp_sini_mjup_min:.5f} M_Jupiter")
print(f"Error in M_p sin(i) ≈ {Mp_sini_mjup_max_error:.5f} %")
print(f"M_p sin(i) ≈ {Mp_sini_mearth:.2f} M_Earth")
print(f"Maximum M_p sin(i) ≈ {Mp_sini_mearth_max:.2f} M_Earth")
print(f"Minimum M_p sin(i) ≈ {Mp_sini_mearth_min:.2f} M_Earth")
print(f"Error in M_p sin(i) ≈ {Mp_sini_mearth_error:.2f} %")
