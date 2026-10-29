#Generate Square Numbers in Range
#Write a Python program to generate and print a list of the first
#  and last 5 elements where the values are square numbers between
# 1 and 30 (both included).

def squares():
    new_list = []
    for i in range(1,31):
        new_list.append(i*i)
    return(new_list)

print(squares()[:5])
print(squares()[-5:])