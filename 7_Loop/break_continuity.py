a = [1, 2, 3, 4, 5, 6, 7, 8]
"""
for item in a:
    print(item)
    if (item == 3):
        break
print("The loop has ended")
"""
for item in a:
    print(item)
    if (item == 4):
        print("Item is equal to 4")
        continue

for i in range(4):
    print("printing")
    if i == 2:
        continue
    print(i)
