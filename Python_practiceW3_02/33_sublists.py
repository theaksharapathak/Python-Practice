#Write a Python program to generate all sublists of a list.
my_list = [1,2,3]
sublists = []

for i in range(len(my_list)):
    for j in range(i+1, len(my_list)+1):
        sublists.append(my_list[i:j])
print(sublists)

    