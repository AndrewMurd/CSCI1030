#Andrew Murdoch
#CSCI 1030U
#Lab4
#2018-11-7

#Question 1
class StudentEntry:
    #Declare object variables
    def __init__(self, name, sid):
         self.name = name
         self.sid = sid
    def average(self, labs, assignments, midterm, finalExam):
        #calculate midterm and final mark
        midterm = midterm * 0.3
        finalExam = finalExam * 0.4
        #average calculate
        self.average = finalExam + labs + assignments + midterm
    def letterGrade(self):
        #return average
        self.average(self.labs,self.assignments,self.midterm,self.final)
        #check for correct mark according to average
        if(self.average < 50):
            return("F")
        if(self.average > 49 and self.average < 60):
            return("D")
        if(self.average > 59 and self.average < 70):
            return("C")
        if(self.average > 69 and self.average < 80):
            return("B")
        if(self.average > 79):
            return("A")

print('Question 1\n')
bsmith = StudentEntry("Bob Smith", "1000001")
bsmith.labs = 9.0
bsmith.assignments = 17.0
bsmith.midterm = 57.5
bsmith.final = 60.0
print("Bob Smith: ", bsmith.letterGrade())
sjones = StudentEntry("Sally Jones", "1000002")
sjones.labs = 9.5
sjones.assignments = 19.5
sjones.midterm = 81.0
sjones.final = 74.5
print("Sally Jones: ", sjones.letterGrade())

#Question 2
class Product:
    #Declare object variables
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        
    def getShippingCost(self, weight):
        #calculate shipping cost
        self.shippingCost = weight * 10
    
    def getTax(self, price):
        #calculate tax
        self.tax = price * 0.13
        
    def getTotalPrice(self):
        #return calculated values
        self.getShippingCost(self.weight)
        self.getTax(self.price)
        #calculate total cost
        totalCost = self.price + self.tax + self.shippingCost
        return totalCost
    
print('Question 2\n')
razor = Product("Electric Razor", 49.99, 0.25)
homeGym = Product("Home Gym", 879.99, 115.0)
print("total cost of", razor.name, ":", razor.getTotalPrice())
print("total cost of", homeGym.name, ":", homeGym.getTotalPrice())

#Question 3
def subset(list1, list2):
    num = 0
    #loop through each element is subset list
    for x in range(len(list1)):
        #pass that value through each value in original list
        for y in range(len(list2)):
            #count how many values are similar
            if (list1[x] == list2[y]):
                num += 1
    #return true or false depending on how many values are similar
    if (num == len(list1)):
        return print("True")
    else:
        return print("False")
    
print('Question 3\n')
subset([1,9,13,15,23], [1,3,5,7,9,11,13,15,17,19,21,23,25])
subset([3,8,13,21,25], [1,3,5,7,9,11,13,15,17,19,21,23,25])

#Question 4
def sublistInRange(list1, minimum, maximum):
    y = 0
    #loop through list
    for x in range(len(list1)):
        #check to see if value passes through max and min
        if (list1[x - y] < minimum or list1[x - y] > maximum):
            #delete value
            del list1[x - y]
            y += 1 
            
    return print(list1)
    
print('Question 4\n')
sublistInRange([1,2,3,4,5], 2, 4)
sublistInRange([5,8,3,21,7,4,14], 4, 14)

#Question 5
def palindromeRec(string): 
    #reverse inputed string
    revString = ''.join(reversed(string)) 
    #check to see if they are same
    if (string == revString): 
        return True
    return False

print('Question 5\n')
print("is level a palindrone?",palindromeRec("level"))
print("is lever a palindrone?",palindromeRec("lever"))      

#Question 6
def jumpMaximum(list1):
    #find max value
    x = max(list1)
    for i in range(len(list1)):
    #find elelement equal to max value
        if (list1[i] == x):
            x = i
            #swap elements
            temp = list1[x]
            list1[x] = list1[0]
            list1[0] = temp
    return print(list1)
    
print('Question 6\n')
jumpMaximum([1,2,3,4])
jumpMaximum([5,8,3,21,7,4,14])

#Question 7
def isReordering(list1, list2):
    #sorting each array to compare
    list1.sort()
    list2.sort()
    for x in range(len(list1)):
        if (list1[x] != list2[x]):
            #return flase if they are exactly the same
            return print("False")
        else: 
            # return true if they are 
            return print("True")

print('Question 7\n')
isReordering([4,1,3,2],[1,2,3,4])
isReordering([5,8,3,21],[5,21,8])