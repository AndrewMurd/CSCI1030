
def frequency(sentence):
    list1 = []
    list2 = list1
    list3 = []
    start = 0
    end = 0
    num = 0
    strNum = ""
    for symbol in sentence:
        end += 1
        if symbol == ' ':
            list1.append(sentence[start:end - 1])
            start = end
    list1.append(sentence[start:len(sentence)])
    
    for x in range(len(list2)):
        for y in range(len(list1)):
            if list1[x] == list1[y]:
                num += 1
        strNum = str(num)
        list3.append(list1[x] + ": " + strNum)
        num = 0
    return list3
    


string_1 = "Apple Mango Orange Mango Guava Guava Mango"
string_2 = "Train Bus Bus Train Train Taxi Aeroplane Taxi Bus"
print(frequency(string_1))
print(frequency(string_2))




