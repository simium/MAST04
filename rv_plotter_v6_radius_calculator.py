import numpy as np

# Known values
transit_depth = 0.0078  # Replace with your actual value
Rs_solar = 0.46       # Star radius in solar radii

# Planet radius in solar radii
Rp_solar = Rs_solar * np.sqrt(transit_depth)

# Convert to Earth radii (1 R☉ ≈ 109 R🜨)
Rp_earth = Rp_solar * 109

print(f"Planet radius ≈ {Rp_solar:.5f} R☉ ≈ {Rp_earth:.2f} R🜨")
