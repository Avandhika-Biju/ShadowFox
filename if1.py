height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)
if bmi >= 30:
    category = "Obesity"
elif 25 <= bmi < 30:
    category = "Overweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
else:
    category = "Underweight"
print("BMI:", round(bmi, 2))
print("Category:", category)  


# output

# Enter height in meters: 1.75
# Enter weight in kilograms: 70
# BMI: 22.86
# Category: Normal
