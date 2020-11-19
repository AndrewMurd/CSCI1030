
#Question 5
class Shape:
    def __init__(self):
        self.numberOfSides = 0
        self.sumOfAngles = 0

    def getNumberOfSides(self):
        return self.numberOfSides

    def getSumOfAngles(self):
        return self.sumOfAngles

    def __str__(self):
        return self.shapeName + ' (# of sides: ' + str(self.numberOfSides) + ', sum of angles: ' + str(self.sumOfAngles) + ')'
        
class Triangle(Shape):
    def __init__(self):
        self.numberOfSides = 3
        self.sumOfAngles = 180
        self.shapeName = 'Triangle'

class Square(Shape):
    def __init__(self):
        self.numberOfSides = 4
        self.sumOfAngles = 360
        self.shapeName = 'Square'

class Pentagon(Shape):
    def __init__(self):
        self.numberOfSides = 5
        self.sumOfAngles = 540
        self.shapeName = 'Pentagon'


triangle = Triangle()
square = Square()
pentagon = Pentagon()
shapes = [triangle, square, pentagon]
for shape in shapes:
    print(shape)

