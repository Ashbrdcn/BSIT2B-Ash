# Using 'from', 'import', and 'as'

# 'import' statement:
# - Imports an entire module.
import math  # Importing the 'math' module

# 'from ... import' statement:
# - Imports a specific function or class from a module.
from random import randint  # Importing only the 'randint' function from 'random'

# 'import ... as' statement:
# - Imports a module and gives it an alias for convenience.
import datetime as dt  # Importing 'datetime' module with alias 'dt'

# Using the imported modules and functions
print("Square root of 16:", math.sqrt(16))  # Uses 'math.sqrt()' to find the square root
print("Random number:", randint(1, 10))  # Generates a random number between 1 and 10
print("Current Date:", dt.datetime.now())  # Retrieves and prints the current date and time
