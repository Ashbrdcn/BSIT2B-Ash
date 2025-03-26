# Using 'break', 'continue', and 'pass' in loops

# 'break' statement:
# - Immediately stops the loop when a specific condition is met.
# - In this case, the loop stops when 'i' is equal to 2.
for i in range(5):
    if i == 2:
        break  # Stops the loop when i is 2
    print(i)

print("---")

# 'continue' statement:
# - Skips the current iteration and moves to the next one.
# - Here, when 'i' is 2, it skips printing and continues with the next value.
for i in range(5):
    if i == 2:
        continue  # Skips iteration when i is 2
    print(i)

print("---")

# 'pass' statement:
# - Acts as a placeholder and does nothing.
# - Useful for defining loops, functions, or conditionals that will be implemented later.
for i in range(5):
    if i == 2:
        pass  # Does nothing, just a placeholder
    print(i)
