# Creating a dictionary
student = {
    "name": "IRIFO",
    "age": 25,
    "course": "software engineering",
    "is_graduated": False
}

# Accessing values
print(student["name"])       # Output: Kenny
print(student["age"])        # Output: 25

# Adding a new key-value pair
student["grade"] = "A"

# Updating a value
student["age"] = 26

# Removing a key-value pair
del student["is_graduated"]

print(student)