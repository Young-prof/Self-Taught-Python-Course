# Write a program to print multiplication table of n using for loop in reversed order
n = 4
for i in range(1, 11):
    j = 11 - i
    print(f"{n} X {j} = {n * j}")
