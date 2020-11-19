

#Question 2
def findSecondMin(values):
    
    values.sort()
    
    return values[1]


list1 = [100,150, 200]
print(findSecondMin(list1))
