# --------------------  20CE042 - SHARAD KEVADIYA --------------------------
# LINK : https://github.com/sharad-999/PIP259

k=int(input())                  # integer input from user
L = input()                     # string input
Li = set(list(L.split(' ')))    # converting string to list and then to set
Li.remove(max(Li))              # finding max element and then removing it from set
print(max(Li))                  #print runner up's score