# Python Strings: Comprehensive Notes with Explanations

# 1. What is a String?
print("1. What is a String?")
# Strings can be defined using single, double, or triple quotes.
single_quote = 'Hello'
double_quote = "World"
triple_quote = '''This is
a multi-line string.'''

print("Single-quoted string:", single_quote)
print("Double-quoted string:", double_quote)
print("Triple-quoted string:", triple_quote)

# 2. String Indexing and Slicing
print("\n2. String Indexing and Slicing")
s = "Python"
print(f"Original String: {s}")

# Indexing
print("Accessing the first character:", s[0])  # First character
print("Accessing the last character:", s[-1])  # Last character

# Slicing
print("Characters from index 0 to 4 (exclusive):", s[0:4])  # Slicing
print("Characters from the start to index 3 (exclusive):", s[:3])
print("Characters from index 2 to the end:", s[2:])
print("Every second character in the string:", s[::2])  # Step in slicing

# 3. String Immutability
print("\n3. String Immutability")
# Strings cannot be modified in place; instead, you create new strings.
s = "Python"
print(f"Original String: {s}")
# Trying to modify it will cause an error.
# s[0] = "J"  # Uncommenting this line will raise an error
s = "Jython"  # Instead, we assign a new value to the variable
print(f"String after reassignment: {s}")

# 4. Common String Methods
print("\n4. Common String Methods")

# Case Conversion Methods
s = "hello world"
print("Original string:", s)
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Title case:", s.title())
print("Capitalized:", s.capitalize())
print("Swapcase:", s.swapcase())

# Whitespace Removal Methods
s = "   hello   "
print("\nOriginal string with spaces:", f"'{s}'")
print("After strip:", f"'{s.strip()}'")
print("After lstrip (left strip):", f"'{s.lstrip()}'")
print("After rstrip (right strip):", f"'{s.rstrip()}'")

# Search and Replace Methods
s = "Python is fun"
print("\nOriginal string:", s)
print("Index of 'is':", s.find("is"))
print("Replacing 'fun' with 'awesome':", s.replace("fun", "awesome"))

# Checking String Properties
s = "Python123"
print("\nString for property checks:", s)
print("Contains only alphabets:", s.isalpha())
print("Contains only digits:", s.isdigit())
print("Contains only alphanumeric characters:", s.isalnum())
print("Contains only whitespace characters:", s.isspace())

# Split and Join Methods
s = "Python is fun"
print("\nOriginal string for splitting and joining:", s)
split_string = s.split()
print("Split string into words:", split_string)
joined_string = " ".join(split_string)
print("Joined words with spaces:", joined_string)

# Checking Start and End of Strings
print("\nChecking the start and end of strings")
print("Does the string start with 'Py'? :", s.startswith("Py"))
print("Does the string end with 'on'? :", s.endswith("on"))

# 5. String Concatenation and Repetition
print("\n5. String Concatenation and Repetition")
s1 = "Hello"
s2 = "World"
print("String 1:", s1)
print("String 2:", s2)
# Concatenation
concatenated = s1 + " " + s2
print("Concatenated string:", concatenated)
# Repetition
repeated = s1 * 3
print("String repeated three times:", repeated)

# 6. String Formatting
print("\n6. String Formatting")

# Using f-strings
name = "John"
age = 25
print("Using f-strings:", f"My name is {name} and I am {age} years old.")

# Using format()
formatted = "My name is {} and I am {} years old.".format(name, age)
print("Using format():", formatted)

# Using % formatting
percent_formatted = "My name is %s and I am %d years old." % (name, age)
print("Using % formatting:", percent_formatted)

# 7. Escape Characters
print("\n7. Escape Characters")
print("Using double quotes inside a string: \"Python is great!\"")
print("Using single quotes inside a string: 'It\'s a great day!'")
print("Using backslash for file paths: C:\\Users\\John")

# 8. Raw Strings
print("\n8. Raw Strings")
raw_string = r"C:\Users\John"
print("Raw string:", raw_string)

# 9. String Operations
print("\n9. String Operations")

# Membership Operators
s = "Python is fun"
print(f"String for operations: {s}")
print("Does the string contain 'Python'? :", "Python" in s)
print("Does the string not contain 'Java'? :", "Java" not in s)

# String Comparison
print("\nString Comparison Examples:")
print("Is 'apple' less than 'banana'? :", "apple" < "banana")
print("Is 'a' greater than 'A'? :", "a" > "A")

# 10. Practical Examples
print("\n10. Practical Examples")

# Reversing a String
s = "Python"
reversed_string = s[::-1]
print(f"Original string: {s}, Reversed string: {reversed_string}")

# Counting Vowels
s = "Hello, World!"
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in s if char in vowels)
print(f"String: {s}, Number of vowels: {vowel_count}")

# Checking Palindrome
palindrome_check = "madam"
is_palindrome = palindrome_check == palindrome_check[::-1]
print(f"Is the string '{palindrome_check}' a palindrome? :", is_palindrome)

# Word Frequency
s = "hello world hello everyone"
words = s.split()
word_frequency = {word: words.count(word) for word in set(words)}
print("Word frequency in the string:", word_frequency)


# Intermediate String Operations

# String formatting with f-strings
name = "Alice"
age = 25
greeting = f"Hello, {name}. You are {age} years old."
print("Formatted String:", greeting)

# Multiline Strings using triple quotes
multiline_str = """This is a multiline string.
It spans across multiple lines."""
print("\nMultiline String:", multiline_str)

# String methods: find, replace, count
sentence = "Python is awesome. Python is easy to learn."
position = sentence.find("awesome")  # Finds the first occurrence of substring
print("\nPosition of 'awesome':", position)

replaced_sentence = sentence.replace("Python", "Java")  # Replace 'Python' with 'Java'
print("Replaced String:", replaced_sentence)

word_count = sentence.count("Python")  # Count occurrences of a word
print("Count of 'Python':", word_count)

# Splitting a String into a List
words = sentence.split()  # Default split by space
print("\nWords List:", words)

# Join a List into a String
words = ["Hello", "World", "Python"]
sentence_from_list = " ".join(words)  # Join elements with space
print("Joined Sentence:", sentence_from_list)

# Slicing Strings
text = "Hello, Python!"
sliced = text[7:13]  # Extract substring from index 7 to 13 (exclusive)
print("\nSliced String:", sliced)

# Checking if String is Palindrome
def is_palindrome(s):
    return s == s[::-1]

word = "madam"
print(f"Is '{word}' a palindrome? {is_palindrome(word)}")

# String methods: upper, lower, strip, isdigit
str_example = "  Hello Python!  "
print("\nUppercase:", str_example.upper())
print("Lowercase:", str_example.lower())
print("Stripped String:", str_example.strip())  # Remove leading/trailing whitespaces
print("Is Digit:", "12345".isdigit())  # Returns True if string is numeric