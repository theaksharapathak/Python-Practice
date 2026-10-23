#Write a Python program to multiply all the items in a list

def multiply_list(items):
    mult_nos = 1
    for item in items:
        mult_nos *= item
    return mult_nos
items = [1,2,3,4]
print(multiply_list(items))
