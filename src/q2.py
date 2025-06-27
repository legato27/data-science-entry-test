def find_and_replace(lst, find_val, replace_val):
 
    if not isinstance(lst, list):
        return -1  # "Input must be a list"
    return_list = []
    
    for item in lst:
        if item == find_val:
            return_list.append(replace_val)
        else:
            return_list.append(item)

    return return_list


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"
