
    
#Question 1
def palindrome(my_str):
    
    myStack = []
    
    for ch in my_str:
        myStack.append(ch)
        
    rev_str = ''
    
    while (len(myStack) != 0):
        
        rev_str = rev_str + myStack.pop()
        
    if (rev_str == my_str):
        return True
    else:
        return False


print(palindrome("aibohphobia"))
print(palindrome("not a palindrome"))