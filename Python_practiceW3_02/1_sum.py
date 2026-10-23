#Write a Python program to sum all the items in a list.
n = [1,2,3] 
def sum_list(n):
    sum_nos = 0
    for i in n:
        sum_nos += i
    return sum_nos

print(sum_list(n))
    