# BMI computation upon user input
myHeight = float(input("Please enter your height in meters: "))
myWeight = float(input("Please enter your weight in kg: "))

bmi = myWeight / (myHeight**2)

print(f"Your bmi is {round(bmi, 2)}")
