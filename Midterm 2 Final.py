

def subset(list1, list2):
    num = 0
    for x in range(len(list1)):
        for y in range(len(list2)):
            if (list1[x] == list2[y]):
                num += 1
    if (num == len(list1)):
        return print("True")
    else:
        return print("False")
    
print('Question 3\n')
subset([4,18,1,12,6], [4,2,18,6,9,12,23,5,1])
subset([12,8,19,4,7], [3,12,8,19])
    
