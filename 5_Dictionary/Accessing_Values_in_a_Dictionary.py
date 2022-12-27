'''
The Same way you access List in python is the same way you acces a Dictionary except for some slite or tracable differences.

To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets, as shown here:
'''
alien_0 = {'color': 'green'}
print(alien_0['color'])
# output green

alien_0 = {'color': 'green', 'points': 5}
'''
Now you can access either the color or the point value of alien_0. If a player shoots down this alien, you can look up how many points they should earn using code like this:
'''
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
