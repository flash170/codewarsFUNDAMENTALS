"""
Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or
non-integer.  If the array does not contain any numbers then you should return 0.
Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2
Input: []
Output: 0
Input: [-2.398]
Output: -2.398
Assumptions
You can assume that you are only given numbers.
You cannot assume the size of the array.
You can assume that you do get an array and if the array is empty, return 0.
What We're Testing
We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
Advanced users may find this extremely easy and can easily write this in one line.
"""

# Initialize array
"""arr = [1, 2, 3, 4, -5];
sum = 0;

# Loop through the array to calculate sum of elements
for i in range(0, len(arr)):
    sum = sum + arr[i];

print("Sum of all the elements of an array: " + str(sum))
"""
# working, dont test passed from codewars
"""
def sum_array(a):
    #a = []
    sum = 0
    for i in range(0, len(a)):
        sum = sum + a[i]
    return(sum)

a = []
#a = [1, 2, 5]
print(sum_array([1, 5.2, -5, 3]))
abc = sum_array([1, 5.2, -5, 3])

print(type(abc))
print(sum_array([]))
print(sum_array([1, 2, 3]))
print(sum_array([1.1, 2.2, 3.3]))
print(sum_array([4, 5, 6]))
print(sum_array(range(101)))
"""


# Working test
"""
Test Results:
Testing sum array
Fixed tests
 (5 of 5 Assertions)
Completed in 0.06ms
You have passed all of the tests! :)
"""

def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return (sum)
arr = []
arr = [12, 3, 4, 15]
n = len(arr)
ans = _sum(arr)
print('Sum of the array is ', ans)
