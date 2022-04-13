# Student Name: Meet Bharodiya
# Student ID:  20CE006

# take input from user
str=input()
str1=""
for i in range(len(str)):
    # to check str[i] is alpha or not
    if str[i].isalpha():
        # covert into uppercase
        if str[i].isupper():
            str1=str1+str[i].lower()
            # covert into uppercase
        if str[i].islower():
            str1=str1+str[i].upper()
    else:
        str1=str1+str[i]
print(str1)
