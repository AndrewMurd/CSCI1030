#Andrew Murdoch
#CSCI 1030U
#Lab7
#2018-10-25

import random
import matplotlib.pyplot as plt
import numpy as np

def binarySearch(array, item, count):
    first = 0
    last = len(array) - 1
    found = False
    
    while(first <= last and not found):
        mid = (first + last)//2
        count += 1
        if array[mid] == item:
            count += 1
            found = True
        else:
            if item < array[mid]:
                count += 1
                last = mid - 1
            else: first = mid + 1
    
    print(found)
    return count


x_array = []
y_array = []
array = []
count = 0
for x in range(8, 49):
    x_array.append(x)
    for y in range(x):
        array.append(random.randint(1, 10))
    print(array)
    item = random.randint(1, 10)
    count = binarySearch(array, item, count)
    y_array.append(count)
    array.clear()

    
plt.title("Complexity Graph of Binary Search")
plt.xlabel("Number of elements")
plt.ylabel("Number of Operations")
plt.plot(x_array, y_array)