# --------------------  20CE042 - SHARAD KEVADIYA --------------------------
# LINK : https://github.com/sharad-999/PIP259

k=int(input())               #input of number of person in group
st=input()                   #input of room no in string
li=list(st.split(" "))       #convert string in list
for x in li:                 #loop in list
    c=li.count(x)            #count for each element in list
    if c==1:                 #captain's room no is repeated once that is checked here
        print(x)             #print captain's room no
