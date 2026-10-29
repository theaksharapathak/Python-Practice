#Remove Duplicates from List
#Write a Python program to remove duplicates from a list.
my_list = [1,2,3,44,44,1,3,90]

def remove_duplicates(items):
    return sorted(set(items))

print("final list:", remove_duplicates(my_list))