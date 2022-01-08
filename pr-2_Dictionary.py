# --------------------  20CE042 - SHARAD KEVADIYA --------------------------
# LINK : https://github.com/sharad-999/PIP259
# ------------------------------   A   -----------------------------------------------
# a. Write a Python script to check whether a given key already exists in a dictionary.
# ------------------------------------------------------------------------------------

# declared dictionary
movie={
    # "key": "value",
    "name":"spiderman",
    "year":2021,
    "rating":4.8,
    "comment":"awesome movie",
}

# take input of key
key=input("enter key to find in dictionary:")

# below for loop will check whether key exist or not
for x in movie:
    if x==key:
        print("key Exist")
    break
else:
    print("key not Exist")

#------- 2nd method------
# if key in movie.keys():
#     print("key is present")
# else :
#     print("key is Not present")

# -----------------------------------   B   -----------------------------------------
# b. Write a Python script to merge two Python dictionaries.
# -----------------------------------------------------------------------------------
book={
    "price":270.80,
    "pages":159
}
# update function will merge two python dictionary
movie.update(book)
print(movie)

# -----------------------------------   C    -----------------------------
# c. Write a Python program to sum all the items in a dictionary.
# ------------------------------------------------------------------------

dict={
    'a':100,
    'b':50,
    'c':50.4
}
# to do sum of value in dictionary we need one list containing all values of dictionary
values=[]  #declared list
for x in dict:
    values.append(dict[x])

# after this for loop we will get list of all values present in dictionary
sum=sum(values)
print(sum)

# --------------------------   D   -----------------------------------
# d. Write a Python script to add a key to a dictionary.
# -------------------------------------------------------------------
dic={
    "0":10,
    "1":20,
}
dic["2"]=30
print(dic)

# -----------------------------------  E   -----------------------------------------
# e. Write a Python script to concatenate following dictionaries to create a new one.
# -----------------------------------------------------------------------------------

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
d4={}
d4.update(dic1)
d4.update(dic2)
d4.update(dic3)
print(d4)