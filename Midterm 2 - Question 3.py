
def frequency(sentence):
    list1 = []
    list2 = []
    dict1 = []
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
    
    list2 = list1
    
    for x in range(len(list1)):
        list2[x] = 0
    
    for x in range(len(list1)):
        if list2[x] == 0:
            for y in range(len(list1)):
                if list1[x] == list1[y]:
                    num += 1
                    list2[x] = 1
            key1 = (list1[x])
            dict1 = {str(key1): num}
            num = 0
    return dict1


string_1 = "Apple Mango Orange Mango Guava Guava Mango"
string_2 = "Train Bus Bus Train Train Taxi Aeroplane Taxi Bus"
print(frequency(string_1))
print(frequency(string_2))




