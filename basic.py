# Python Basics: Introduction and Syntax

# 1. Python as an Interpreted Language
# Python executes code line by line, making it easy to debug and test.

# 2. Comments in Python
# Single-line comment: Use #
# Multi-line comment: Use triple quotes

# Single-line comment
print("Single-line comment example.")  # Inline comment

# Multi-line comment
'''
This is a multi-line comment.
Useful for adding detailed explanations in code.
'''
print("Multi-line comment example.")

# 3. Variables and Data Types
name = "Alice"   # String
age = 25         # Integer
height = 5.5     # Float
is_student = True  # Boolean

print("Name:", name, "| Age:", age, "| Height:", height, "| Is student:", is_student)

# 4. Input and Output
# Taking input
user_input = input("Enter your name: ")
print("Hello,", user_input)

# 5. Type Conversion
number = "123"  # String
converted_number = int(number)  # Convert to integer
print("Converted Number:", converted_number, "| Type:", type(converted_number))

# Intermediate Python Basics

# List comprehensions for creating new lists
# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print("List of squares:", squares)

# Ternary Conditional Expressions
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)

# Multiple assignments
x, y, z = 1, 2, 3
print("Multiple assignments - x:", x, "y:", y, "z:", z)

# Using any() and all()
numbers = [1, 2, 3, 4, 5]
print("Any number > 4:", any(x > 4 for x in numbers))  # Returns True if any condition is True
print("All numbers > 0:", all(x > 0 for x in numbers))  # Returns True if all conditions are True