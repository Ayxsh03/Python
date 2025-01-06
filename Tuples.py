# Python Tuples: Immutable Sequences

# 1. Creating Tuples
coordinates = (10, 20, 30)
print("Coordinates:", coordinates)

# 2. Accessing Elements
print("First coordinate:", coordinates[0])

# 3. Slicing
print("Last two coordinates:", coordinates[-2:])

# 4. Tuple Packing and Unpacking
point = (1, 2, 3)  # Packing
x, y, z = point    # Unpacking
print(f"Unpacked: x={x}, y={y}, z={z}")

# 5. Tuple Methods
print("Count of 1:", point.count(1))
print("Index of 2:", point.index(2))

# Intermediate Tuple Operations

# Creating Tuples
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)

# Accessing Tuple Elements
print("\nElement at index 2:", my_tuple[2])
print("Slicing Tuple (1 to 3):", my_tuple[1:4])

# Nested Tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("\nNested Tuple:", nested_tuple)
print("Accessing nested element:", nested_tuple[1][1])

# Tuple Methods: count, index
print("\nCount of 3 in Tuple:", my_tuple.count(3))  # Count occurrences of a value
print("Index of 4 in Tuple:", my_tuple.index(4))  # Get the index of an element

# Unpacking Tuples
a, b, c, d, e = my_tuple  # Unpacking into variables
print("\nUnpacked Values:", a, b, c, d, e)

# Concatenation and Repetition of Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2  # Concatenate tuples
repeated_tuple = tuple1 * 3  # Repeat tuple elements
print("\nConcatenated Tuple:", concatenated_tuple)
print("Repeated Tuple:", repeated_tuple)

# Tuple as a Return Value
def get_coordinates():
    return (10, 20)  # Returning a tuple

x, y = get_coordinates()
print("\nCoordinates:", x, y)