# Write a program to greet all the person naes stored in a list l1 and which starts with T
#       l1 = ["Frank", "Tekenatei", "Perezitei", "Deepka", "Telma the Foody"]


l1 = ["Frank", "Tekenatei", "Perezitei", "Deepka", "Telma the Foody"]

for item in l1:
    if item.lower().startswith("t"):
        print(f"Good Morning {item}")
