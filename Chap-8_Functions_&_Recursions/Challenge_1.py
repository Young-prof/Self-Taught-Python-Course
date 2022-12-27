# Write a program using function to find greatest of three numbers

def greatestNum(num1, num2, num3):
    if(num1 > num2):
        greatest = num1
    else:
        greatest = num2
    if(num3 > greatest):
        greatest = num3
    return greatest

result = greatestNum(324, 44, 34)
print(result)