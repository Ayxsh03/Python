# Object-Oriented Programming: Classes and Objects in Python

# Defining a Class
class Person:
    """A simple class to represent a person."""

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display information
    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

    # Method with behavior
    def is_adult(self):
        return self.age >= 18

# Creating Objects
john = Person("John Doe", 25)
jane = Person("Jane Doe", 16)

# Accessing Attributes and Methods
print("Accessing Attributes and Methods:")
print(john.display())
print("Is John an adult?", john.is_adult())
print(jane.display())
print("Is Jane an adult?", jane.is_adult())

# Inheritance
class Employee(Person):
    """Class to represent an employee, inheriting from Person."""

    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display(self):
        return f"{super().display()}, Employee ID: {self.employee_id}"

# Creating a Derived Class Object
print("\nInheritance:")
emp = Employee("Alice", 30, "E123")
print(emp.display())

# Encapsulation
class BankAccount:
    """Class to represent a bank account."""

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    # Public method to access private attribute
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

# Using Encapsulation
print("\nEncapsulation:")
account = BankAccount("John Doe", 1000)
print("Initial Balance:", account.get_balance())
account.deposit(500)
print("Updated Balance:", account.get_balance())

# Intermediate OOPs Concepts: Class Inheritance, Polymorphism, Method Overriding, and Class Methods

# Inheritance and Method Overriding
class Animal:
    def speak(self):
        return "Animal sounds"

class Dog(Animal):
    def speak(self):  # Overriding the speak method
        return "Woof"

# Polymorphism: Using the same method name but getting different behavior
dog = Dog()
print("Dog says:", dog.speak())  # Calls Dog's speak() method

# Class Methods and Static Methods
class Calculator:
    @classmethod
    def add(cls, a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print("\nClass method add:", Calculator.add(3, 5))
print("Static method multiply:", Calculator.multiply(3, 5))

# Encapsulation: Private and Public Methods
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print("\nAccount balance:", account.get_balance())