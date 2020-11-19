
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

