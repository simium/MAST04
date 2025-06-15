import numpy as np

# Constants
R_sun = 6.957e8      # meters
AU = 1.496e11        # meters

# Given values
T_s = 3350                     # K
R_s = 0.46 * R_sun             # star radius in meters
a = 0.028675 * AU              # semi-major axis in meters

# Function to compute equilibrium temperature
def T_eq(albedo):
    return T_s * np.sqrt(R_s / (2 * a)) * (1 - albedo)**0.25

# Calculate for A = 0 and A = 0.3
T_eq_A0 = T_eq(0.0)
T_eq_A03 = T_eq(0.3)
T_eq_A_Jup = T_eq(0.343)

# Output
print(f"Equilibrium Temperature (A = 0.0) : {T_eq_A0:.1f} K")
print(f"Equilibrium Temperature (A = 0.3) : {T_eq_A03:.1f} K")
print(f"Equilibrium Temperature (A = 0.343) : {T_eq_A_Jup:.1f} K")
