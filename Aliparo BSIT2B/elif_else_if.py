# Using 'if', 'elif', 'else'

# 'if' statement:
# - Evaluates a condition and executes the block if the condition is True.
num = 15  

if num < 10:
    # Executes if 'num' is less than 10
    print("Less than 10")

# 'elif' statement:
# - Checks another condition if the previous 'if' condition was False.
elif num == 15:
    # Executes if 'num' is exactly 15
    print("Exactly 15")

# 'else' statement:
# - Executes if none of the above conditions are True.
else:
    # Executes if 'num' is greater than 10 but not 15
    print("Greater than 10 but not 15")
