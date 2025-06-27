def check_divisibility(num, divisor):
    
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return False #Ensure it is numeric"
        
    if divisor == 0: #Cannot divide by zero.
        return False
        
    is_divisible = (num % divisor == 0)
    return is_divisible


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
