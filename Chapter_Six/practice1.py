# Write a program to find gratest of four numbers entered by the user
a = 35
b = 333
c = 93
d = 23

# if (a > b and a > c and a > d):
#     print("A is the greatest")
# elif (b > c and b > c and b > d):
#     print("b is the greatest")
# elif (c > a and c > b and c > d):
#     print("c is the greatest")
# elif (d > a and d > b and d > c):
#     print("d is the greatest")
# else:
#     print("There is no matching Number")

if (a > b):
    maxNum1 = a
else:
    maxNum1 = b
if (c > d):
    maxNum2 = c
else:
    maxNum2 = d
if (maxNum1 > maxNum2):
    max1 = maxNum1
else:
    max1 = maxNum2
print("the Maximum number is", max1)
