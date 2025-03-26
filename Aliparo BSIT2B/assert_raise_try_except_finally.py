# Using 'assert', 'raise', 'try', 'except', 'finally'

def divide(a, b):
    assert b != 0, "Denominator cannot be zero!"  # AssertionError if b is 0
    return a / b

try:
    result = divide(10, 0)
except AssertionError as e:
    print("Assertion Error:", e)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed.")

# Using 'raise'
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above!")
    return "Access granted"

try:
    print(check_age(16))
except ValueError as e:
    print("Error:", e)
