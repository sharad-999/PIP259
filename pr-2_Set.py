# --------------------  20CE042 - SHARAD KEVADIYA --------------------------
# LINK : https://github.com/sharad-999/PIP259

# ------------------------------   A   -----------------------------------------------
# a. Write a Python program to add member(s) in a set and clear a set
# ------------------------------------------------------------------------------------

# set cotains only distinct value
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
