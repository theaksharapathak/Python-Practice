# Write a Python program to generate and print a
#  list of the first and last 5 elements where the
#  values are square numbers between 1 and 30 (both included).
def square_nos():
    l = []
    for i in range(1, 31):
        l.append(i*i)
    return l


print(square_nos()[:5])
print(square_nos()[-5:])
