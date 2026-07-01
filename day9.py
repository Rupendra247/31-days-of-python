# Day 9: Tuples & Sets

# 1. Tuples (Immutable)
coordinates = (40.7128, 74.0060)
# coordinates[0] = 10  # This would raise a TypeError!

# Tuple Unpacking: Extremely useful in Python
lat, lon = coordinates
print(f"Latitude: {lat}, Longitude: {lon}")

# 2. Sets (Unique & Unordered)
ids = {101, 102, 103, 101} # 101 will only appear once!
ids.add(104)

# Set Operations (Math logic)
group_a = {1, 2, 3}
group_b = {3, 4, 5}
print(f"Union (all unique): {group_a | group_b}")
print(f"Intersection (common): {group_a & group_b}")