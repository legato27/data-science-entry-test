def find_first_negative(lst):
    
    if not isinstance(lst, list):
        return -1
    
    i = 0
    while i < len(lst):   
        if not isinstance(lst[i], (int, float)): 
            return -1
        if lst[i] < 0:
            return lst[i]
        i += 1
        
    return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
