import numpy as np

# Constants
M_jup = 1.898e27      # kg
R_earth = 6.371e6     # meters

# Given values
Mp_jup = 0.069
Rp_earth = 4.5

# Convert to SI
Mp = Mp_jup * M_jup
Rp = Rp_earth * R_earth

# Compute volume and density
volume = (4/3) * np.pi * Rp**3
density = Mp / volume

# Output
print(f"Planet mass:   {Mp:.3e} kg")
print(f"Planet radius: {Rp:.3e} m")
print(f"Planet density: {density:.1f} kg/m³")
