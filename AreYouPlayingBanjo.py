"""
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo"
name + " does not play banjo"
Names given are always valid strings.
"""
a = "Rikki"
b = "Yura"
c = "room"
d = "Kira"

print(a[0])

first = c[0]
print(first)
if first == "R" or "r":
    print(c + " " + "plays banjo")
else:
    print(c + " " + "does not play banjo")
