def swap(x, y):
       
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
        
    x, y = y, x  
    print(f"{x} , {y}")
    
    return x, y
    
