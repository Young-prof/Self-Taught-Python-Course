'''
You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
'''

myInvites = ['Seri', 'Future Wife', 'Loved ones']

notAbletoAttend = 'Seri'  # When using the remove method, do not forget to First of all store the element you want to remove into a sepereate variable before continuing
myInvites.remove(notAbletoAttend)
SerinotAbletoAttend = f"{notAbletoAttend} will not be able to attend the Dinner"
print(SerinotAbletoAttend)

myInvites.append('Gina')
print(myInvites)


Gbaby = f"Hey {myInvites[0]}, Please if you could go on a dinner with me i'll love it"
print(Gbaby)

futureWife = f"Hey {myInvites[1]}, How bout you come have a dinner with with"
print(futureWife)

loved = f"this is a special invitation for all of my {myInvites[2]}"
print(loved)


# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.

print("Hello everyone, please i've found a bigger dinner table")

# • Use insert() to add one new guest to the beginning of your list.
myInvites.insert(0, 'Miracle')
Mimi = f"{myInvites[0]} I'm inviting you for a Home Party"
print(Mimi)
# • Use insert() to add one new guest to the middle of your list.
myInvites.insert(2, 'Chioma')
Chibaby = f"{myInvites[2]}, What's up with you, I'm having a home party this weekend, I'm inviting you"
print(Chibaby)

# • Use append() to add one new guest to the end of your list.
myInvites.append('Ijeoma')
IjeBaby = f"{myInvites[5]} i dy invite you for my house party"
print(IjeBaby)
# • Print a new set of invitation messages, one for each person in your list.
