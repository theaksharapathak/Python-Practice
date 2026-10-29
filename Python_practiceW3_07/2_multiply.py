#Multiply Items in List
my_list = [1,2,3,4]

def multiply_list():
    multiply = 1
    for i in my_list:
        multiply*= i
    return multiply

print(multiply_list())