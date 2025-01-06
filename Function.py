# Functions: Reusable Blocks of Code

# Defining a Function
def greet(name):
    """Function to greet a person by name."""
    return f"Hello, {name}!"

# Calling the Function
print("Calling greet():", greet("Alice"))

# Default Arguments
def power(base, exponent=2):
    """Function with default arguments."""
    return base ** exponent

print("\nDefault Argument Function:")
print("2^3:", power(2, 3))  # Using both arguments
print("2^2:", power(2))  # Using the default value for exponent

# Keyword Arguments
print("\nKeyword Arguments:")
print("3^4:", power(exponent=4, base=3))

# Variable-Length Arguments (*args and **kwargs)
def summary(*args, **kwargs):
    """Function with variable-length arguments."""
    print("Positional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)

print("\nVariable-Length Arguments:")
summary(1, 2, 3, a=4, b=5)

# Lambda Functions
square = lambda x: x ** 2
print("\nLambda Function:")
print("Square of 5:", square(5))

# Higher-Order Functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))  # Using map with lambda
print("\nHigher-Order Function:")
print("Squared Numbers:", squared_numbers)

# Intermediate Functions

# Functions with variable-length arguments
def my_sum(*args):
    return sum(args)

print("Sum of numbers:", my_sum(1, 2, 3, 4, 5))

# Lambda Functions with multiple arguments
multiply = lambda x, y: x * y
print("Multiplication result:", multiply(3, 4))

# Recursion: A function calling itself
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# Higher-order function: Functions that take other functions as arguments
def apply_function(f, x):
    return f(x)

result = apply_function(lambda x: x**2, 5)  # Applying a square function
print("Applying a function:", result)

# Closures: Functions that remember the environment in which they were created
def outer(x):
    def inner(y):
        return x + y
    return inner

closure = outer(10)
print("Closure result:", closure(5))