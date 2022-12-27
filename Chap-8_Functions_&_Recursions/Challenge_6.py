# write a python function to print first n lines of the following pattern
def printPatters(n):
    for i in range(n):
        print('*' * (n-i))


printPatters(4)
