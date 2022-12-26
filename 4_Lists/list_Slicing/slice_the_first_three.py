'''
Slice the first three elements of the following Variable
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])

'''
To slice the second third and last elements of the variable
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

'''
If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

'''
A similar syntax works if you want a slice that includes the end of a list. For example, if you want all items from the third item through the last item, you can start with index 2 and omit the second index:
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
