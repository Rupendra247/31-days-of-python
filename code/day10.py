# Day 10: Dictionaries
# Structure: {key: value}

user_profile = {
    "username": "coder123",
    "email": "coder@example.com",
    "skills": ["Python", "JavaScript"],
    "is_active": True
}

# Accessing data
print(f"User email: {user_profile.get('email')}")

# Modifying and Adding
user_profile["last_login"] = "2026-07-02"
user_profile["skills"].append("SQL")

# Iterating through dictionaries
# .items() is the most powerful way to loop through both keys and values
for key, value in user_profile.items():
    print(f"{key.capitalize()}: {value}")

# Deleting
del user_profile["is_active"]