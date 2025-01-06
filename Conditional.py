# Python Conditional Statements: if, elif, else

# 1. Basic if statement
age = 18
if age >= 18:
    print("You are an adult.")

# 2. if-else statement
marks = 70
if marks >= 50:
    print("You passed!")
else:
    print("You failed!")

# 3. if-elif-else statement
grade = 85
if grade >= 90:
    print("Grade: A")
elif grade >= 75:
    print("Grade: B")
elif grade >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# 4. Nested if
number = 15
if number > 0:
    if number % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")