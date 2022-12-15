# write a program to find weather a given number is prime or not

num = 10
for i in range(2, num):
    if (num % i == 0):
        print("Num is a prime")
        break
else:
    print("Num is not a prime")
