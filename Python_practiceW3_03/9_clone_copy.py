#Write a Python program to clone or copy a list.
my_list = [1,2,3]

def copied_list(items):
    new_list = []
    for i in items:
        new_list.append(i)
    return new_list
print("original list:",my_list)
print("copied list:",copied_list(my_list))