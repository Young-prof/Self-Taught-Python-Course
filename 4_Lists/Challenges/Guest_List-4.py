'''
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
'''

myInvites = ['Seri', 'Future Wife', 'Loved ones']

notAbletoAttend = 'Seri'  # When using the remove method, do not forget to First of all store the element you want to remove into a sepereate variable before continuing
myInvites.remove(notAbletoAttend)
SerinotAbletoAttend = f"\n{notAbletoAttend} will not be able to attend the Dinner"
print(SerinotAbletoAttend)

myInvites.append('Gina')
print(myInvites)


Gbaby = f"\nHey {myInvites[0]}, Please if you could go on a dinner with me i'll love it"
print(Gbaby)

futureWife = f"\nHey {myInvites[1]}, How bout you come have a dinner with with"
print(futureWife)

loved = f"\nthis is a special invitation for all of my {myInvites[2]}"
print(loved)


# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.

print("\nHello everyone, please i've found a bigger dinner table")

# • Use insert() to add one new guest to the beginning of your list.
myInvites.insert(0, 'Miracle')
Mimi = f"{myInvites[0]} I'm inviting you for a Home Party"
print(Mimi)
# • Use insert() to add one new guest to the middle of your list.
myInvites.insert(2, 'Chioma')
Chibaby = f"\n{myInvites[2]}, What's up with you, I'm having a home party this weekend, I'm inviting you"
print(Chibaby)

# • Use append() to add one new guest to the end of your list.
myInvites.append('Ijeoma')
IjeBaby = f"\n{myInvites[5]} i dy invite you for my house party"
print(IjeBaby)
# • Print a new set of invitation messages, one for each person in your list -- For the previous part of the project

# For the Guest_List-4 part of the project

# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
print("\nHello Everyone, please i'm o sorry for inconviencing you'll. I only have space for two")

# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
print(myInvites)  # The original list
Mira = myInvites.pop(0)  # Popped out
messageToMira = f"\n{Mira} I'm so sory for dissapointing please forgive me, i have only two tables for the party"
print(messageToMira)
print(myInvites)  # The list After the poping

Chichi = myInvites.pop(1)
messageToChichi = f"\n{Chichi} I'm so sory for dissapointing please forgive me, i have only two tables for the party"
print(messageToChichi)
print(myInvites)

Ggirl = myInvites.pop(2)
messageToGgirl = f"\n{Ggirl} I'm so sory for dissapointing please forgive me, i have only two tables for the party"
print(messageToGgirl)
print(myInvites)

ije = myInvites.pop(2)
messageToIje = f"\n{ije} I'm so sory for dissapointing please forgive me, i have only two tables for the party"
print(messageToIje)
print(myInvites)

# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
del myInvites[0]
del myInvites[0]
print(myInvites)
