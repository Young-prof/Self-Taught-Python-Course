# You can loop over all the values in a tuple using a for loop, just as you did with a list:

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

'''
In python you can’t modify a tuple, you can assign a new value to a variable that represents a tuple. So if we wanted to change our dimensions, we could redefine the entire tuple:
'''
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (800, 400)
print('\nNew Dimenstions')
for dimension in dimensions:
    print(dimension)
