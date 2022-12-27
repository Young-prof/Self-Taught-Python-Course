'''
Using keys in square brackets to retrieve the value you’re interested in from a dictionary might cause one potential problem: if the key you ask for doesn’t exist, you’ll get an error. 

Let’s see what happens when you ask for the point value of an alien that doesn’t have a point value set:
'''
'''
We saw that this results in an error
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])
'''

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
# If the there is no message that is 'No point value assigned' is not given, then it will return None
