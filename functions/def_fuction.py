def calculate_bmi(mass = 56, height = 1.5):
    """ This function calculates the BMI of a person based on the height in meters and mass in kilograms that they provided """
    BMI = mass / (height**2)
    return BMI

bodymassindex = calculate_bmi(78, 1.5)
print(bodymassindex)

if bodymassindex >= 18.5 and bodymassindex <= 24.9:
    print("Your BMI is within the healthy range.")
else:
    print("Your BMI is not within the healthy range.")

bmi2 = calculate_bmi(height = 1.5, mass = 78)
print(bmi2)

bmi3 = calculate_bmi()
print(bmi3)


