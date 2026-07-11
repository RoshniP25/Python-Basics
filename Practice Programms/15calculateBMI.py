print("==== BODY MASS INDEX (BMI) CALCULATOR ====")

#inputs
name = input("Enter your name: ")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

#formula: BMI = weight / (height * height)
bmi = weight / (height ** 2)

print(f"\n{name}, Your BMI is: {bmi}")