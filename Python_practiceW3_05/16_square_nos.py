#Generate Square Numbers in Range
#Write a Python program to generate and print a list of the first 
# and last 5 elements where the values are square numbers between 1 and
#  30 (both included).

n = 30

def square_nos(n):
    new_list = []
    for i in range(1, n+1):
        new_list.append(i*i)
    return new_list

print(square_nos(n)[:5])
print(square_nos(n)[-5:]) 