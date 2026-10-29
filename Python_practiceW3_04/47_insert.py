#Insert Element Before Each List Item
#Write a Python program to insert an element before each element of a list.
my_list = ['cat', 'dog','coffee']
n=5
new_list = []
for i in my_list:
    new_list.append(n)
    new_list.append(i)

print(new_list)
