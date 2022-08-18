"""
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
"""

"""def bmi(weight, height):
    i = weight/(height**2)"""

weight = 50
height = 1.67
bmi = weight/(height**2)
print(bmi)

if bmi <= 18.5:
    print("Underweight")
elif bmi <= 25.0:
        print("Normal")
elif bmi <= 30.0:
        print("Overweight")
elif bmi > 30.0:
        print("Obese")
else:
    print("no data")


