#Write a Python program to insert an element before each element of a list.
my_list = ['p','q','r']
n = 3
new_list = []
for i in my_list:
    new_list.append(n)
    new_list.append(i)

print(new_list)