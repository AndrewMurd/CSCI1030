#Andrew Murdoch
#CSCI 1030U
#Lab4
#2018-10-10

#PART 1
lst1 = [1,3,5,7,9,11,13,15,17,19,21,23,25]
lst2 = [1,4,9,16,25]
lst3 = set()

#intersection function
def intersection(lst1, lst2): 
    #loop between lists to find equivilent 
    for x in lst1:
        for y in lst2:
            if (x == y):
                lst3.add(y)
    
    return lst3

#Output intersected list
print(intersection(lst1, lst2))

#PART 2
def estimate_pi(terms):
    result = 0.0
    #loop for amount of terms
    for n in range(terms):
        #calculate using equation
        result += (-1.0)**n/(2.0*n+1.0)
    #return result
    return 4*result

#Output PI
print(estimate_pi(10000000))

#PART 3
def drawTri(a):
    #Declaring Variables
    num = 1
    starSpot = 0
    rowCount = 0
    spaceCount = 1
    output= ""
    #Loop for given value
    while (num <= a):
        while (rowCount < a):
            if (num == a):
                #print bottom row(base of trianle)
                output = output + '*'
    
            else:
                if (num > 1):
                    #starting point of hypotenus
                    starSpot = a - num
                    #print hypotenus
                    if (rowCount == starSpot):
                        output = output + '*'
                    #print left side of triangle
                    elif (rowCount == (a-1)):
                        output = output + '*'
                    #print number of spaces    
                    else:
                        output = output + ' '
                #else       
                else:
                    if (rowCount == (a-1)):
                        output = output + '*'
                    else:
                        output = output + ' '
            #increase the rows each loop               
            rowCount = rowCount + 1
            #increase amount of spaces
            spaceCount = spaceCount + 1
        #the count
        num = num + 1
        rowCount = 0
        
        #Output the result
        print(output)
        #reset output
        output = ""
    
#input both triangles    
print(drawTri(7))
print(drawTri(13))

    
