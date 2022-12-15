# Wrte a program to print the following star Pattern
"""
the star pattern takes this form
            *
          *   *
        *   *   *
     *      *      *
"""
n = int(input("Enter a number: "))
for i in range(1, n):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    for j in range(n-i):
        print(" ", end="")
    print("\n", end="")
