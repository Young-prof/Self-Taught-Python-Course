'''
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
•   Start with your Guest_List-2.py. Add a print() call at the end of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list.
'''

myInvites = ['Seri', 'Future Wife', 'Loved ones']

notAbletoAttend = 'Seri'  # When using the remove method, do not forget to First of all store the element you want to remove into a sepereate variable before continuing
myInvites.remove(notAbletoAttend)
SerinotAbletoAttend = f"{notAbletoAttend} will not be able to attend the Dinner"
print(SerinotAbletoAttend)

myInvites.append('Gina')
print(myInvites)

# Seri = f"Hey {myInvites[0]}, So I've been wondering if you could go out on a dinner with me" Seri has been removed from the original list because she is not attending
# print(Seri)
Gbaby = f"Hey {myInvites[0]}, Please if you could go on a dinner with me i'll love it"
print(Gbaby)

futureWife = f"Hey {myInvites[1]}, How bout you come have a dinner with with"
print(futureWife)

loved = f"this is a special invitation for all of my {myInvites[2]}"
print(loved)
