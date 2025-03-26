# Using 'class', 'def', 'return', and 'yield'

# 'class' keyword:
# - Defines a blueprint for creating objects.
# - In this case, 'Person' class represents a person with a name and a greeting method.
class Person:
    def __init__(self, name):
        # '__init__' is the constructor method that initializes object attributes.
        self.name = name  

    def greet(self):
        # 'return' statement:
        # - Sends back a value from a function.
        # - This method returns a formatted greeting string.
        return f"Hello, my name is {self.name}!"

# Function with 'return':
# - Takes two numbers as input and returns their sum.
def add(a, b):
    return a + b  # Returns the sum of 'a' and 'b'

# Generator function using 'yield':
# - Unlike 'return', 'yield' allows the function to return values one at a time and continue execution.
def count_up(n):
    for i in range(1, n + 1):
        yield i  # Returns values one at a time, pausing execution

# Creating an instance of the 'Person' class and calling its method
p = Person("Ash")
print(p.greet())  # Outputs: Hello, my name is Ash!

# Calling the 'add' function and printing the result
print(add(5, 10))  # Outputs: 15

# Iterating over the generator function and printing each value
for num in count_up(3):
    print(num)  # Outputs: 1, 2, 3 (one at a time)
