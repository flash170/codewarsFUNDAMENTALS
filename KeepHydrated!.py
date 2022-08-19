"""
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5

"""

# worked with out func

"""time = 11.8

liters = time * 0.5

print(int (liters))"""


# working with func
def litres(time):
    liters = time * 0.5
    return int(liters)


print(litres(11.8))
