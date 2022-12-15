# write a program to calculate the factorial of a given number using for loop.

# Using Conditional statements
import math
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print(" Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial*i
    print("The factorial of", num, "is", factorial)


# Using built-function----Advanced5

def fact(n):
    return (math.factorial(n))


num = int(input("Enter the number:"))
f = fact(num)
print("Factorial of", num, "is", f)


# Using Recursion---Advanced
def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)


num = 5
print("Factorial of", num, "is",)
fact(num)
