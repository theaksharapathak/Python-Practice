#Multiply Items in List
#Write a Python program to multiply all the items in a list.

l = [1,2,3,4]

def multiply_list(items):
    multiply = 1
    for i in items:
        multiply *=i
    return multiply


print(multiply_list(l))
