
sub1 = int(input("Enter marks for Mathematics\n"))
sub2 = int(input("Enter marks for English\n"))
sub3 = int(input("Enter marks for Biology\n"))
sub4 = int(input("Enter marks for Chemistry\n"))
sub5 = int(input("Enter marks for Physics\n"))

sum = sub1 + sub2 + sub3 + sub4 + sub5
average = sum/5


if average >= 91 and average <= 100:
    print("Your Grade is A+",sum)
elif average >= 81 and average <= 90:
    print("Your Grade is A", sum)
elif average >= 71 and average <= 80:
    print("Your Grade is B+", sum)
elif average >= 61 and average <= 70:
    print("Your Grade is B", sum)
elif average >= 51 and average <= 60:
    print("Your Grade is C+", sum)
elif average >= 41 and average <= 50:
    print("Your Grade is C", sum)
elif average >= 31 and average <= 40:
    print("Your Grade is D+", sum)
elif average >= 21 and average <= 30:
    print("Your Grade is D", sum)
elif average >= 0 and average <= 20:
    print("Your Grade is E", sum)
else:
    print("Invalid Input!")

if average >= 41 and average <= 100:
    print("You are Promoted to the next class")
else:
    if average >= 0 and average <= 40:
        print("You are not Promoted to the next class") 