#Multiply Items in List

def multiply(items):
    multiply_nos = 1
    for item in items:
        multiply_nos *= item
    return multiply_nos
print(multiply([2,3,2]))