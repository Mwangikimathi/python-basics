num = 100
name = "jane"
#print(10 >= 11 and num % 6 != 0 or len(name) <= 10)

names = ["Jane","John","Mary",'Joseph',"Mark"]
#print("John" not in names)

age =int(input("What is your age?\n"))
gender = input("What is your gender?\n")
if gender == "male" and age >= 18:
    print("You're a male,Welcome to our club")
elif gender == "female" and age >= 21:
    print("You are a female,Welcome to our club")
else:
    print("Incorrect Input")



