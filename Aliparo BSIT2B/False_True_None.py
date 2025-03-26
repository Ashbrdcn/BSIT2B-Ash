# Using 'False', 'True', and 'None'

# 'True' and 'False' are Boolean values used in logical operations.
x = True   # Represents a truthy value
y = False  # Represents a falsy value

print("x:", x)  # Outputs: x: True
print("y:", y)  # Outputs: y: False

# 'None' is a special constant in Python that represents the absence of a value.
def check_value(val):
    # Checks if the passed value is 'None'
    if val is None:
        return "No value provided"  # Returns this if val is None
    return f"Value is {val}"  # Returns the value if it's not None

print(check_value(None))  # Outputs: No value provided
print(check_value(10))    # Outputs: Value is 10
