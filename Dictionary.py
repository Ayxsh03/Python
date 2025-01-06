# Dictionaries: Key-Value Pair Data Structure in Python

# Creating a Dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Original Dictionary:", person)

# Accessing Values
print("\nAccessing Values:")
print("Name:", person["name"])  # Access using key
print("Age:", person.get("age"))  # Using get() method

# Adding or Updating Entries
print("\nAdding/Updating Entries:")
person["email"] = "john@example.com"  # Adding a new key-value pair
person["age"] = 31  # Updating an existing key
print("Updated Dictionary:", person)

# Removing Entries
print("\nRemoving Entries:")
person.pop("email")  # Removes a key-value pair
print("After pop:", person)
del person["city"]  # Deletes a key-value pair
print("After del:", person)

# Dictionary Methods
print("\nDictionary Methods:")
print("Keys:", person.keys())  # Get all keys
print("Values:", person.values())  # Get all values
print("Items:", person.items())  # Get all key-value pairs

# Iterating through a Dictionary
print("\nIterating through Dictionary:")
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")

# Nested Dictionaries
print("\nNested Dictionaries:")
nested_dict = {
    "employee1": {"name": "Alice", "age": 25},
    "employee2": {"name": "Bob", "age": 30},
}
print("Nested Dictionary:", nested_dict)
print("Accessing Nested Value:", nested_dict["employee1"]["name"])

# Intermediate Dictionary Operations

# Dictionary comprehension: create a dictionary from a list of tuples
pairs = [("apple", 1), ("banana", 2), ("cherry", 3)]
fruit_dict = {key: value for key, value in pairs}
print("Dictionary from comprehension:", fruit_dict)

# Merging Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}  # Merging using unpacking
print("Merged Dictionary:", merged_dict)

# Using defaultdict from collections
from collections import defaultdict
default_dict = defaultdict(int)
default_dict["apple"] += 1
default_dict["banana"] += 2
print("Default dictionary:", dict(default_dict))

# Dictionary with lambda functions
person = {
    "name": "Alice",
    "age": 25,
    "job": "Engineer"
}
sorted_person = sorted(person.items(), key=lambda x: x[1])
print("Sorted dictionary by values:", sorted_person)