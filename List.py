# Python Lists: Creation, Methods, and Examples

# 1. Creating Lists
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# 2. Accessing List Elements
print("First fruit:", fruits[0])  # Indexing
print("Last fruit:", fruits[-1])  # Negative indexing

# 3. List Slicing
print("First two fruits:", fruits[:2])  # Slicing

# 4. Adding Elements
fruits.append("orange")  # Append
fruits.insert(1, "blueberry")  # Insert
print("After adding fruits:", fruits)

# 5. Removing Elements
fruits.remove("banana")  # Remove by value
popped = fruits.pop()    # Remove last element
print("Popped fruit:", popped, "| Remaining fruits:", fruits)

# 6. Other Methods
numbers = [3, 1, 4, 1, 5]
numbers.sort()  # Sort
numbers.reverse()  # Reverse
print("Sorted and reversed numbers:", numbers)

# 7. List Comprehension
squares = [x**2 for x in range(5)]
print("Squares using list comprehension:", squares)

# Intermediate List Operations

# List Comprehensions with Conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]  # List of even numbers
print("Even Numbers:", even_numbers)

# List slicing
my_list = [0, 1, 2, 3, 4, 5, 6]
print("\nSliced List (1 to 4):", my_list[1:5])  # List from index 1 to 4 (exclusive)
print("List from beginning to index 3:", my_list[:4])  # List from start to index 3
print("List from index 3 to end:", my_list[3:])  # List from index 3 to the end

# Modifying List elements
my_list[2] = 100  # Change element at index 2
print("\nModified List:", my_list)

# Adding and Removing Elements
my_list.append(10)  # Add an element at the end
print("After append:", my_list)

my_list.insert(1, 50)  # Insert at a specific index
print("After insert:", my_list)

my_list.remove(100)  # Remove an element by value
print("After remove:", my_list)

popped_value = my_list.pop()  # Remove the last element
print("Popped value:", popped_value)
print("After pop:", my_list)

# List concatenation and repetition
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2  # Concatenation
repeated_list = list1 * 2  # Repetition
print("\nConcatenated List:", concatenated_list)
print("Repeated List:", repeated_list)

# List methods: sort, reverse, index, and count
numbers_list = [4, 2, 7, 1, 9, 3, 8]
numbers_list.sort()  # Sort the list
print("\nSorted List:", numbers_list)

numbers_list.reverse()  # Reverse the list
print("Reversed List:", numbers_list)

index_of_7 = numbers_list.index(7)  # Find the index of a value
print("Index of 7:", index_of_7)

count_of_3 = numbers_list.count(3)  # Count occurrences of a value
print("Count of 3:", count_of_3)

# Nested Lists
nested_list = [[1, 2], [3, 4], [5, 6]]
print("\nNested List:", nested_list)
print("Accessing element [1][1]:", nested_list[1][1])  # Access inner list and element