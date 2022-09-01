"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the
string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""

a = "This is an example!"
x = a.split(" ")
#print(a)

"""
print(x[0])
stringlength = len(x[0])
slicedString = x[0][stringlength::-1]
print(slicedString)

print(stringlength)"""

for i in range(0, len(x)):
    stringlength = len(x[i])
    slicedString = x[i][stringlength::-1]
    if i != len(x) -1:
        slicedString += " "
    print(slicedString)

