counter = 0
num = List[0]
for i in List:
The count() method returns the number of occurrences of a number in the given List.
    curr_frequency = List.count(i)
    if(curr_frequency> counter):
        counter = curr_frequency
        num = i
print("Number which is repeted most: ")
print(num)
print("Frequency of most repeted number is: ")
print(counter)