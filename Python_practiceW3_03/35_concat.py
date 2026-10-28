#Write a Python program to create a list by concatenating a given 
# list with a range from 1 to n.
my_list = ['cat','dog','cake']
n = int(input("enter a no:"))
new_list = []

def concat_list(items):
    for i in range(1,n+1):
        for j in items:
            new_list.append(j+str(i))
    return new_list


print("New list:", concat_list(my_list))