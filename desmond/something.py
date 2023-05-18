x = 5

def outer_func():
    y = 3
    
    def inner_func():
        z = x + y
        return z
    
    return inner_func()