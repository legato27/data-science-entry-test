def string_reverse(s):
    if not isinstance(s, str):
        return -1  # or raise ValueError("Input must be a string.")
    
    return s[::-1] 


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
