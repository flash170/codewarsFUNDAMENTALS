"""
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
"""

"""def bmi(weight, height):
    i = weight/(height**2)"""
# with out function

"""weight = 50
height = 1.67
bmi = round(weight/(height**2), 1)
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
"""

"""def bmi(weight, height):
    bmii = round(weight / (height ** 2), 1)
    if bmii <= 18.5:
        print("Underweight")
    elif bmii <= 25.0:
        print("Normal")
    elif bmii <= 30.0:
        print("Overweight")
    elif bmii > 30.0:
        print("Obese")
    else:
        print("NoutTTT")
    return bmii




print(bmi(50, 1.80))"""

# Correct  resuly
"""
Test Results:
Log
Normal
Fixed Tests
Basic Test Cases
 (5 of 5 Assertions)
Completed in 0.06ms
You have passed all of the tests! :)
"""
def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5 : return "Underweight"
    elif bmi <= 25 : return "Normal"
    elif bmi <= 30 : return "Overweight"
    else: return "Obese"


print(bmi(70, 1.7))

