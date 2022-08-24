"""
Grade book
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
"""

"""a = 58
b = 56
c = 51

if 90 <= a and b and c <= 100:
    print("A")
elif 80 <= a and b and c < 90:
    print("B")
elif 70 <= a and b and c < 80:
    print("C")
elif 60 <= a and b and c < 70:
    print("D")
elif 50 <= a and b and c < 60:
    print("F")
else:
    print("Error")"""


def get_grade(s1, s2, s3):
    if 90 <= (s1 + s2 + s3)/3 <= 100:
        return "A"
    elif 80 <= (s1 + s2 + s3)/3 < 90:
        return "B"
    elif 70 <= (s1 + s2 + s3)/3 < 80:
        return "C"
    elif 60 <= (s1 + s2 + s3)/3 < 70:
        return "D"
    elif 0 <= (s1 + s2 + s3)/3 < 60:
        return "F"
    else:
        print("Error")


print(get_grade(65, 61, 69))
