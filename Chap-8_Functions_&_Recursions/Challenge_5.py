# Write a recursive function to calculate the sum of first n natural numbers.
# Sum(8) = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
# Sum(n) = (n-1) + n
def Sum(n):
    if (n == 1):
        return 1
    return Sum(n-1) + n


result = Sum(8)
print(result)
