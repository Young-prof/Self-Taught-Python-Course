# Write a program which finds out whether a given name is present in a list or not

# Using the in keyword

myList = ["a", "b", "c", "d"]

print("Our list is", myList)

if ("a" in myList):
    print("a is in myList")
else:
    print("a is not in myList")

# Using the not in keyword

MyList = ['a', 'b', 'c', 'd', 'e']

print("Our List: ", MyList)

# Check if 'a' exists in the list or not
if 'a' not in MyList:
    print(" item 'a' is not present in the list")
else:
    print(" 'a' is present in the list")
