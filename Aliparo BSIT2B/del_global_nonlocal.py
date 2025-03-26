# Using 'del', 'global', and 'nonlocal'

# 'global' keyword:
# - Used to modify a global variable inside a function.
x = 10  # Global variable

def modify_global():
    global x  # Refers to the global 'x' and modifies its value
    x = 20  # Changes the global variable

modify_global()
print("Updated global x:", x)  # Outputs: Updated global x: 20

# 'nonlocal' keyword:
# - Used to modify a variable from an enclosing (non-global) scope.
def outer():
    y = 5  # Enclosing variable

    def inner():
        nonlocal y  # Refers to 'y' from the outer function and modifies it
        y += 1
        print("Inner y:", y)  # Outputs: Inner y: 6

    inner()
    print("Outer y:", y)  # Outputs: Outer y: 6

outer()

# 'del' keyword:
# - Deletes a variable or an element from a data structure.
z = [1, 2, 3]  # List with three elements
del z[1]  # Deletes element at index 1 (value 2)
print("After deletion:", z)  # Outputs: After deletion: [1, 3]
