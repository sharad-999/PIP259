# --------------------  20CE042 - SHARAD KEVADIYA --------------------------
# LINK : https://github.com/sharad-999/PIP259

# ------------------------------   A   -----------------------------------------------
# a. Write a Python program to add member(s) in a set and clear a set
# ------------------------------------------------------------------------------------

# set cotains only distinct value
from typing import List


set= {2,3,4}
# before adding element
print(set)
# add 5 in set
set.add(5)
# after adding element
print(set)


# -----------------------------------   B   -----------------------------------------
# b. Write a Python program to remove an item from a set if it is present in the set.
# -----------------------------------------------------------------------------------
set={1,2,3,5,7}
x=int(input("Enter Number to remove from Set :"))
for i in set :
    if(i==x):
        set.remove(x)
        print(x," removed from set")
        print(set)
        break
    print(i)
else:
    print(x," Not found")

#  --------  2nd Method :--------
# if x in set :
#     set.remove(x)
#     print("Sucessfully removed")
#     print(set)
# else :
#     print(x," Not Found in set")


# -----------------------------------   C    --------------------------------------
# c. Write a Python program to create an intersection, Union, difference of sets.
# ---------------------------------------------------------------------------------

A={1,2,3,5,7,4,9}
B={2,4,6,8,10}
# intersection method is used to find intersection 
# it will return the intersection of two set as a new set
print("intersection of A and B :",A.intersection(B))
# Union will return the Union of two set as a new set
print("Union of A and B :",A.union(B))
# Difference will return the Difference of two set as a new set
print("difference of A and B :",A.difference(B))


# --------------------------   D   ---------------------------------------------
# d. Write a Python program to find maximum and the minimum value in a set.
# ------------------------------------------------------------------------------
A={2,26,56,4,3,-2,55,0}
print("Max in set :",max(A))
print("Min in Set :",min(A))


# -----------------------------------   E   -------------------------------------------------------------------
# e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary
# -------------------------------------------------------------------------------------------------------------

List = [2, 1, 2, 2, 1, 3]
counter = 0
num = List[0]
for i in List:
# The count() method returns the number of occurrences of a number in the given List.
    curr_frequency = List.count(i)
    if(curr_frequency> counter):
        counter = curr_frequency
        num = i
print("Number which is repeted most: ")
print(num)
print("Frequency of most repeted number is: ")
print(counter)

# method 2
# print(max(List,key=List.count))


# count frequency in tuple
tuple = (1, 2, 4, 5, 6, 6, 3, 6, 8, 3, 6)
L=list(tuple)
counter1 = 0
num1 = L[0]
for i in L:
# The count() method returns the number of occurrences of a number in the given Tuple.
    curr_frequency = L.count(i)
    if(curr_frequency> counter1):
        counter1 = curr_frequency
        num1 = i
print("Number which is repeted most: ")
print(num1)
print("Frequency of most repeted number is: ")
print(counter1)


# count frequency in Dictionary
dic = {1: 'meet', 2: 'harmi', 3: 'sharad', 4: 'aniket', 5: 'jay',
       6: 'sharad', 7: 'harmi', 8: 'sharad', 9: 'bhavdeep'}
# values() method returns list of all values which are in dictionary
value=dic.values()
# convert values in list to count frequncy
l1=list(value)
counter1 = 0
name= list(l1[0])
for i in l1:
    curr_frequency = l1.count(i)
    if(curr_frequency> counter1):
        counter1 = curr_frequency
        name = i
print("Name which is repeted most: ")
print(name)
print("Frequency of most repeted name is: ")
print(counter1)
