'''
You can also use a dictionary to store one kind of information about many objects. For example, say you want to poll a number of people and ask them what their favorite programming language is. A dictionary is useful for storing the results of a simple poll, like this:
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Let's say for instance we wants to know Sarah's Favourite programing language
language = favorite_languages['sarah'].title()
print(f"Sarahs favourite programming language is {language}")
