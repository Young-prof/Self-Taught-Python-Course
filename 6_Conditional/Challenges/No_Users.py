'''
No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.
'''
userNames = []

if userNames:

    for userName in userNames:
        if userName == 'Admin':
            print(
                f"\nHello {userName}, Would you like to see a status report?")
        else:
            print("\nHello " + userName + " Thank you for logging in again")
else:
    print("We need to find some Users!")
