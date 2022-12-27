'''
Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the change.
• The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
'''
BuffetFoods = ('Egusi', 'Draw Soup', 'Fried Rice', 'White Rice and Stew')
for AvailableFoods in BuffetFoods:
    print(AvailableFoods)

    '''
• Try to modify one of the items, and make sure that Python rejects the change.
    
    '''
# AvailableFoods[0] = 'Jollof Rice'
# print(AvailableFoods)


'''
• The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

'''
BuffetFoods = ('yello Soup', 'Draw Soup', 'Rice',
               'White Rice and Stew', 'Bango soup')
for AvailableFoods in BuffetFoods:
    print(AvailableFoods)
