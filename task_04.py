def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

print(swap(5, 10))

def swap(a, b):
    a = a * b
    b = a / b
    a = a / b
    return a, b

print(swap(5, 10))

