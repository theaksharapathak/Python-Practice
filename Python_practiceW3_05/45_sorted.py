#Convert Pairs to Sorted Unique Array
#Write a Python program to convert a pair of values into a sorted unique
#  array.
l = [(1,2),(33,7),(99,2)]
new_list = []
for pairs in l:
    for num in pairs:
        if num not in new_list:
            new_list.append(num)

new_list.sort()

print(new_list)