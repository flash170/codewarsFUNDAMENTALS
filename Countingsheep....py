"""
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the
number  of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined
"""

"""sheep = [False,  True,  True,  False]
print(sheep.count(True))"""
# print("True in {}".format(sheep.index(True)))
"""
for i in range(0, len(sheep)):
    if sheep[i]:
        m = sheep[i]
        print(m)
        """


def count_sheeps(sheep):
    return sheep.count(True)


print(count_sheeps([False, True, True, False]))
