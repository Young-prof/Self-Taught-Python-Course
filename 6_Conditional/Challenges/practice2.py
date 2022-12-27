
mark1 = int(input("Enter the marks for sub 1: "))
mark2 = int(input("Enter the marks for sub 2: "))
mark3 = int(input("Enter the marks for sub 3: "))

totalScore = (mark1 + mark2 + mark3) / 3

if (totalScore >= 40):
    if (mark1 >= 33 and mark2 >= 33 and mark3 >= 33):
        print("You have passed, because your score is greater than 33")
    else:
        print("You did not pass because your score in each subject is below 33")
else:
    print("You have not passed the exam because your score is below 40%")
