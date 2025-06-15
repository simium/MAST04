# Given values
Ms = 0.45           # Stellar mass in solar masses
P_days = 2.6439     # Orbital period in days

# Convert period to years
P_years = P_days / 365.25

# Calculate semi-major axis (in AU)
a_au = (Ms * P_years**2)**(1/3)

print(f"Calculated semi-major axis: {a_au:.6f} AU")
