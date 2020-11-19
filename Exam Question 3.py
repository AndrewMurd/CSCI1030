
#Question 3
def getVowel(string):
    
    my_str = ''
    
    for char in string: 
        if char == 'a':
            my_str = my_str + 'a'
        elif char == 'e':
            my_str = my_str + 'e'
        elif char == 'i':
            my_str = my_str + 'i'
        elif char == 'o':
            my_str = my_str + 'o'
        elif char == 'u':
            my_str = my_str + 'u'
    
    return my_str


print(getVowel('this is a sentence'))
print(getVowel('computer science'))
print(getVowel('i like pizza'))

