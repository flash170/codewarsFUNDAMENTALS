"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the
string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""

a = "This is an example!"
x = list(a.split(" "))
#print(a)

"""
print(x[0])
stringlength = len(x[0])
slicedString = x[0][stringlength::-1]
print(slicedString)

print(stringlength)"""

"""for i in range(0, len(x)):
    stringlength = len(x[i])
    slicedString = x[i][stringlength::-1]
    if i != len(x) - 1:
        slicedString += " "
    print(slicedString)
    #print(type(slicedString))"""

def reverse_words(text):
  return ' '.join(word[::-1] for word in text.split(" "))


print(reverse_words("This is an example!"))



def reverse_words(str):
  #go for it
  newStr = []
  for i in str.split(' '):
      newStr.append(i[::-1])
  return ' '.join(newStr)

print(reverse_words("This is an example!"))