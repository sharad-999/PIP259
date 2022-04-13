# Student Name: Meet Bharodiya
# Student ID:  20CE006

k=int(input())
lst=[]
for i in range(k):
    str=input()
    # put all strings in list
    lst.append(str)  
for i in lst:
    #count frequency of all string which are in list
    fre=lst.count(i)
    #filter will remove all ith element which are repete in list again
    lst=list(filter((i).__ne__, lst))
    if fre!=0:
        print(fre,end=" ")

