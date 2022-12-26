Template = '''
    Dear <|name|>, 
    you are selected
    <|date|>
'''
name = input("Enter the name: ")
date = input("Enter the date: ")

print(Template.replace('<|name|>', name).replace('<|date|>', date))
