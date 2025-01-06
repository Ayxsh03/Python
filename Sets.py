# Sets: Unordered, Unique Collection of Elements

# Creating a Set
fruits = {"apple", "banana", "cherry"}
print("Original Set:", fruits)

# Adding Elements
print("\nAdding Elements:")
fruits.add("orange")
print("After add:", fruits)

# Removing Elements
print("\nRemoving Elements:")
fruits.remove("banana")  # Raises an error if the element doesn't exist
print("After remove:", fruits)
fruits.discard("mango")  # Does not raise an error if the element doesn't exist
print("After discard:", fruits)

# Set Operations
print("\nSet Operations:")
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1.union(set2))  # Combine all unique elements
print("Intersection:", set1.intersection(set2))  # Common elements
print("Difference (set1 - set2):", set1.difference(set2))  # Elements in set1 but not in set2
print("Symmetric Difference:", set1.symmetric_difference(set2))  # Elements in either set1 or set2, but not both

# Iterating through a Set
print("\nIterating through a Set:")
for fruit in fruits:
    print(fruit)


# Intermediate Set Operations

# Set Comprehensions
squared_set = {x**2 for x in range(10)}
print("Squared Set:", squared_set)

# Set Operations with more sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Union, Intersection, Difference, and Symmetric Difference
print("Union of set1 and set2:", set1 | set2)
print("Intersection of set1 and set2:", set1 & set2)
print("Difference of set1 and set2:", set1 - set2)
print("Symmetric Difference of set1 and set2:", set1 ^ set2)

# Using frozenset (Immutable Set)
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
print("Frozenset Operations:", frozenset1 & frozenset2)  # Intersection of frozensets