#Write a Python program to check if a list is empty or not.
my_list = []

def check_list(items):
    if len(items)==0:
        print("list is empty")
    else:
        print("list is not empty")

check_list(my_list)
