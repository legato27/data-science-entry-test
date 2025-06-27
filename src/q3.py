def update_dictionary(dct, key, value):
    
    if not isinstance (dct, dict):
        return -1
        
    if key in dct:
        print(f"Original value: {dct[key]}")
        dct[key] = value
        
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
