'''
For example, imagine we have a list of our favorite foods and want to make a separate list of foods that a friend likes. This friend likes everything in our list so far, so we can create their list by copying ours:
'''

my_Foods = ['Pizza', 'Cucumba', 'Orange', 'Carrot']
print("My friends favourite foods:\n ")
print(my_Foods)
friends_food = my_Foods[:]
print("My friends favourite foods are:\n ")
print(friends_food)
