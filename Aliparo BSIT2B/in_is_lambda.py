# Using 'in', 'is', and 'lambda'

# 'in' operator:
# - Checks if a value exists within a sequence (like a list, tuple, or string).
nums = [1, 2, 3, 4, 5]  

print(3 in nums)  # True (3 is present in the list)
print(6 in nums)  # False (6 is not in the list)

# 'is' operator:
# - Checks if two variables refer to the same object in memory.
a = None  
b = None  

print(a is b)  # True (Both variables reference the same None object)

# 'lambda' function:
# - Defines a small anonymous function in a single line.
square = lambda x: x * x  # A function that returns the square of x
print("Square of 5:", square(5))  # Outputs: Square of 5: 25
