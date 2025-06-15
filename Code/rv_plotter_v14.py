import numpy as np
import matplotlib.pyplot as plt

# Constants
Ms = 0.45
L_ratio = Ms**3.5

# HZ for Sun (Kasting 1993)
hz_in_sun = 0.95
hz_out_sun = 1.37

# HZ scaled for your star
hz_in_scaled = hz_in_sun * np.sqrt(L_ratio)
hz_out_scaled = hz_out_sun * np.sqrt(L_ratio)

# Planet positions and sizes
planets = [
    ("Mercury", 0.39, 0.38),
    ("Venus",   0.72, 0.95),
    ("Earth",   1.00, 1.00),
    ("Mars",    1.52, 0.53)
]

# Your exoplanet
exo_a = 0.028675
exo_r = 4.5

# Create plot
plt.figure(figsize=(10, 2))
ax = plt.gca()

# HZ for Sun
plt.axvspan(hz_in_sun, hz_out_sun, color='green', alpha=0.2, label='HZ (Sun)')

# HZ for your star
plt.axvspan(hz_in_scaled, hz_out_scaled, color='blue', alpha=0.2, label='HZ (0.45 M☉)')

# Solar system planets
for name, a, r in planets:
    plt.scatter(a, 0, s=r**2*10, label=name)

# Your exoplanet
plt.scatter(exo_a, 0, s=exo_r**2*10, color='red', edgecolors='black', label='Your Planet', zorder=5)

# Labels and legend
plt.xlabel("Distance from star (AU)")
plt.title("Habitable Zones (Kasting 1993): Sun vs 0.45 M☉ Star")
plt.yticks([])
plt.xlim(0, 2)
plt.grid(axis='x')
plt.legend(loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1.3))

plt.tight_layout()
plt.show()
