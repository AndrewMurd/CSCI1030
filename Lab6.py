#Andrew Murdoch
#CSCI 1030U
#Lab4
#2018-10-25
import random
import matplotlib.pyplot as plt

'''
size = 15
unsorted_arr = []
unsorted_arr2 = []
for x in range(size):
    unsorted_arr.append(random.randint(1, 101))
    unsorted_arr2.append(random.randint(1, 101))
    
plt.title("Random Plot")
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")

plt.plot(unsorted_arr, unsorted_arr2, 'r-',
         unsorted_arr2, unsorted_arr, 'b*')
''' 

def insertionSort(alist, count):
   count = 0 
   for index in range(1, len(alist)):

     currentvalue = alist[index]
     position = index

     while position > 0 and alist[position - 1] > currentvalue:
         count += 2
         alist[position] = alist[position - 1]
         position = position - 1

     alist[position] = currentvalue
   return count


x_array = []
y_array = []
unsort = []
count = 0
for x in range(8, 49):
    x_array.append(x)
    for y in range(x):
        unsort.append(random.randint(1, 10))
    print(unsort)
    count = insertionSort(unsort, count)
    y_array.append(count)
    print(unsort)
    unsort.clear()

    
plt.title("Complexity Graph of Insertion Sort")
plt.xlabel("Number of elements")
plt.ylabel("Number of Operations")
plt.plot(x_array, y_array, 'r-')

