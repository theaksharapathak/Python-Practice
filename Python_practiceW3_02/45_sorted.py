# Write a Python program to convert a pair of
# values into a sorted unique array.
l = [(1, 2), (3, 4), (1, 2), (89, 98)]
new_list = []
for pair in l:
    for num in pair:
        if num not in new_list:
            new_list.append(num)
new_list.sort()
print(new_list)
