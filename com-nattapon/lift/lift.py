import random

user_layer = int(input())
list_lift =[]                        
randomlist = []

for x in range(0,5):        
    randomlist.append(random.randint(0,26))

for i in range(5):
    if i > = 0 and i < 5:
        X = user_layer - randomlist[i] 
        Y = abs(X)
        list_lift.append(Y)
        i += 1

min_near_lift = min(list_lift)
index = list_lift.index(min_near_lift)
index += 1
 
print(index)