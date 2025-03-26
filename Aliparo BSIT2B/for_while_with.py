# Using 'for', 'while', and 'with'

# 'for' loop:
# - Iterates over a sequence (like a range, list, or string).
for i in range(3):  
    print("For loop iteration:", i)  # Outputs 0, 1, 2

# 'while' loop:
# - Repeats a block of code as long as the condition is True.
count = 0  
while count < 3:  
    print("While loop count:", count)  # Outputs 0, 1, 2
    count += 1  # Increments count to eventually stop the loop

# 'with' statement:
# - Used for resource management (e.g., file handling) to ensure proper cleanup.
with open("sample.txt", "w") as file:  
    # Opens 'sample.txt' in write mode and automatically closes it after the block
    file.write("Hello, this is a test file.")  # Writes text to the file
