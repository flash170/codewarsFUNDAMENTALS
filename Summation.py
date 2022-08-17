"""
Summation
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer
greater than 0.

For example:

summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
"""


# Passed Test =)

"""
Test Results:
Fixed tests
Basic Test Cases
 (5 of 5 Assertions)
Completed in 0.18ms
You have passed all of the tests! :)
"""

def summation(num):
    total = 0
    for  number in range(1, num + 1):
        total += number
    return total


print(summation(1))
print(summation(8))
print(summation(22))
print(summation(100))
print(summation(213))
