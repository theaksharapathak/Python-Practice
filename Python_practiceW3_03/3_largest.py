# Write a Python program to get the largest number from a list.
my_list = [1, 2, 99]
largest_no = my_list[0]

for i in my_list:
    if i > largest_no:
        largest_no = i

print(largest_no)
