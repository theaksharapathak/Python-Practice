l = [12,2,4]

def multiply_fn(items):
    multiply = 1
    for i in items:
        multiply*= i
    return multiply

print(multiply_fn(l))