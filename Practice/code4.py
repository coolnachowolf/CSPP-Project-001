import random 

def maxValue(lst):
    largest = 0
    for i in range(0, len(lst)):
        if(lst[i] > largest):
            largest = lst[i]
    return largest
    
a = [23, 54, 65, 32]   
print(maxValue(a))
b = random.randint(1,8)
a.append(b)
print(a)
