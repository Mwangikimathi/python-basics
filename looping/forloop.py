#ages = [10, 20, 40, 50, 90, 100]

# sum = 0

# for age in ages:
#     if age > 30:
#         sum = sum + age

# print(sum)

# for item in range(1, 101):
#     if item % 2 == 0:
#         print(item)

number = int(float(input("Enter a number?\n")))   
if number > 0:
    print (number)

    for i in range(1 ,number + 1):
        print(str(i) + " multiplied by " + str(number) + " is " + str(i * number))
else:
    print("Please enter a positive number")

 