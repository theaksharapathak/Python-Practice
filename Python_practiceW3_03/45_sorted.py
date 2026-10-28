#Write a Python program to convert a pair of values into a
#  sorted unique array.
my_list = [(1,2),(44,3),(100,2),(9,8)]
new_list = []

for pair in my_list:
    for num in pair:
        if num not in new_list:
            new_list.append(num)
new_list.sort()
print(new_list)
