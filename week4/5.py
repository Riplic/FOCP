def multiply(a, b=None):
    if b is None:
        return a*a
    else:
        return a*b
    
print(multiply(2))
print(multiply(2,4))
