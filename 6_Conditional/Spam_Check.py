# A spam comment is defined as a text containing the following keywords:
#     "make a lot money", "buy now", "subscribe this", "clck this". Write a program to detect these spams


spamWords = ['buy now', 'subscribe this', 'clck this']


# email = 'this is nice stock. You need to clck this and buy this stock now'
email = input("Enter your email: ").lower()
spam = False
if ("buy now" in email):
    spam = True
if ("subscribe this" in email):
    spam = True
if ("click this" in email):
    spam = True
print("Spam is ", spam)
