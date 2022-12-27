# Write a program to calculate the grade of a student from his marks from the following schem:
# 90 - 100 -> Excellent
# 80 - 90 -> A
# 70 - 80 -> B
# 60 - 70 -> C
# 50 - 60 -> D
# 50 < F
"""
print("Enter the marks obtained in each subject")
mak1 = int(input())
mak2 = int(input())
mak3 = int(input())
mak4 = int(input())
mak5 = int(input())
mak6 = int(input())
toTal = mak1 + mak2 + mak3 + mak4 + mak5 + mak6
avg = toTal / 6

if (avg >= 90 and avg <= 100):
    print("Excellent")
if (avg >= 80 and avg <= 90):
    print("A")
if (avg >= 70 and avg <= 80):
    print("B")
if (avg >= 60 and avg <= 70):
    print("C")
if (avg >= 50 and avg <= 60):
    print('D')
if (avg < 50):
    print("F")
"""
# Second method using a For Loop

mark = []
tot = 0
print("Enter Marks Obtained in 5 Subjects: ")
for i in range(5):
    mark.insert(i, input())

for i in range(5):
    tot = tot + int(mark[i])
avg = tot/5

if avg >= 91 and avg <= 100:
    print("Your Grade is A1")
elif avg >= 81 and avg < 91:
    print("Your Grade is A2")
elif avg >= 71 and avg < 81:
    print("Your Grade is B1")
elif avg >= 61 and avg < 71:
    print("Your Grade is B2")
elif avg >= 51 and avg < 61:
    print("Your Grade is C1")
elif avg >= 41 and avg < 51:
    print("Your Grade is C2")
elif avg >= 33 and avg < 41:
    print("Your Grade is D")
elif avg >= 21 and avg < 33:
    print("Your Grade is E1")
elif avg >= 0 and avg < 21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")
