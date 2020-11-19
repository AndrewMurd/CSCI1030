#Andrew Murdoch
#CSCI 1030U
#Lab9
#2018-11-19

import math

class Shape:
    def __init__(self):
        print("Wooo a constructor")
    
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height
        return area
    
    def getPerimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter

rec1 = Rectangle(10, 20)
rec2 = Rectangle(5, 10)
rec3 = Rectangle(15, 20)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def getArea(self):
        area = math.pi * math.sqrt(self.radius)
        return area
    
    def getPerimeter(self):
        perimeter = 2* (math.pi) * self.radius
        return perimeter
    
cir1 = Circle(5)
cir2 = Circle(10)
cir3 = Circle(15)

shapes = [rec1, rec2, rec3, cir1, cir2, cir3]

for shape in shapes:
    print(shape.getArea(), shape.getPerimeter())



    
    
    
