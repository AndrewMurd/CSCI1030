

#Question 1
class pet:
    def __init__(self, name):
        self.name = name

class Dog(pet):
    def speak(self):
        print (self.name, "-", "Woof!")

class Cat(pet):
    def speak(self):
        print (self.name, "-", "Meow!")

class Bird(pet):
    def speak(self):
        print (self.name, "-", "Cheep!")
  
print('\nQuestion 1\n')      
bird2 = Bird("Yappy")
cat1 = Cat("Boots")
cat2 = Cat("Mr. Fluffington")
cat3 = Cat("Sylvester")
dog1 = Dog("Spot")
dog2 = Dog("Odie")
dog3 = Dog("Charles")
pets = [cat1, dog1, dog2, cat2, bird2, dog3, cat3]
for pet in pets:
    pet.speak()

        
#Question 2
def getWords(sentence):
    list1 = []
    start = 0
    end = 0
    for symbol in sentence:
        end += 1
        if symbol == ' ':
            list1.append(sentence[start:end - 1])
            start = end
    list1.append(sentence[start:len(sentence)])
    return list1

print('\nQuestion 2\n')
print (getWords("He's the hero Gotham deserves, but not the one it needs right now"))

#Qestion 3

class Shape:
    def __init__(self):
        self.numberOfSides = 0
        self.sumOfAngles = 0
        
class Triangle(Shape):
    def __init__(self):
        self.name = "Triangle"
        self.numberOfSides = 3
        self.sumOfAngles = 180
        
    
        
    def __str__(self):  
       return self.name + "(# of sides: " + str(self.numberOfSides) + ", sum of angles: "+ str(self.sumOfAngles) + ")"

class Square(Shape):
    def __init__(self):
        self.name = "Square"
        self.numberOfSides = 4
        self.sumOfAngles = 360
    
    
        
    def __str__(self): 
        return self.name + "(# of sides: " + str(self.numberOfSides) + ", sum of angles: "+ str(self.sumOfAngles) + ")"
    
class Pentagon(Shape):
    def __init__(self):
        self.name = "Pentagon"
        self.numberOfSides = 5
        self.sumOfAngles = 540
    
    
        
    def __str__(self):
        return self.name + "(# of sides: " + str(self.numberOfSides) + ", sum of angles: "+ str(self.sumOfAngles) + ")"
    
print('\nQuestion 3\n')
triangle = Triangle()
square = Square()
pentagon = Pentagon()
shapes = [triangle, square, pentagon]
for shape in shapes:
    print(shape)
    
#Question 4
    
def getReverseWords(sentence):
    words = []
    word = ''
    for i in range(len(sentence) - 1, -1, -1):
        if sentence[i] == ' ':
            words.append(word)
            word = ''
        else:
            word = sentence[i] + word
            
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            words.append(word)
            break
        else:
            word = sentence[i] + word
            
    
    return words
    
print('\nQuestion 4\n')
print(getReverseWords('the quick brown fox jumped over the lazy dog'))
print(getReverseWords("He's the hero Gotham deserves, but not the one itneeds right now"))
    

print('\nQuestion 9\n')
print(zipMultiply([1,2,3], [4,5,6]))
print(zipMultiply([4,3,7], [2,0,7]))
print(zipMultiply([2,4,6,8,10], [1,3,5,7,9]))
    
def computeTotal(items, discounts):
    subtotal = 0
    if (len(items) == len(discounts)):
        for i in range(len(items)):
            disc = items[i] - (items[i] * (discounts[i]/100))
            clearanceDisc = disc - disc * (25/100)
            subtotal += clearanceDisc
        if (subtotal < 50):
            subtotal -= 5
        elif(subtotal >= 50) and (subtotal <= 150):
            subtotal -= 15
        elif(subtotal > 150):
            subtotal -= 30
        return subtotal
    return "Invalid input."

print('\nQuestion 10\n')
print(computeTotal([50.99, 70.99], [25, 50]))
print(computeTotal([15.99, 43.75, 68.25], [10, 35, 20]))
print(computeTotal([40.25, 24.99], [10]))




