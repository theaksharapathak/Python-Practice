#Convert Pairs to Sorted Unique Array
#Write a Python program to convert a pair of values into a sorted unique
#  array.
my_list = [(2,33),(9,89),(45,2)]
new_list = []
for pairs in my_list:
    for num in pairs: 
        if num not in new_list:
            new_list.append(num)

new_list.sort()

print(new_list)