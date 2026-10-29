#Write a Python program to multiply all the items in a list.
l = [1,2,3,4]
mult = 1

def multiply(items):
    
    for i in items:
        mult *= i
    return mult

print(multiply(l))