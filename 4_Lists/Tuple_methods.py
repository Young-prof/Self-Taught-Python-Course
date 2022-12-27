tupleMethod = (1, 7, 2)
print(tupleMethod.count(1))
print(tupleMethod.index(2))

'''
We define the tuple dimensions at u, using parentheses instead of square brackets. At v we print each element in the tuple individually, using the same syntax we’ve been using to access elements in a list:
'''

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

'''
The following code will result to an erro because Tuples work a bit differently with Lists
'''
dimension = (200, 50)
dimension[0] = 250
print(dimension)
