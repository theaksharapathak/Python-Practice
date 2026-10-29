#Generate All List Permutations
#Write a Python program to generate all permutations of a 
# list in Python.
import itertools
my_list = [1,23,34]

print(list(itertools.permutations(my_list)))