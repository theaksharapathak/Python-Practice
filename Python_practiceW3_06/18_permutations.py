#Generate All List Permutations
#Write a Python program to generate all permutations of a list in Python.
import itertools
my_list = [1,22,35]

print(sorted(itertools.permutations(my_list)))