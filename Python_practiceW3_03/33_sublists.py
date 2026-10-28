#Write a Python program to check whether a list contains a sublist.
my_list = [1,2,23]
sublists = []

for i in range(len(my_list)):
    for j in range(i+1, len(my_list)+1):
        sublists.append(my_list[i:j])

print(sublists)