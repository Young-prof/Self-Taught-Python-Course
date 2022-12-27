'''
In this Example we want to use factorial to understand recursive functions
factorial(n) = n * factorial(n-1)
factorial(4) = 4 x 3 x 2 x 1
factorial(3) = 3 x 2 x 1
factorial(13) = 13 x 12 x 11 x 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1
'''


def factorial(n):
    # we setup a base condtion
    if (n == 0 or n == 1):
        return 1
    return n * factorial(n - 1)


a = factorial(3)
print(a)
