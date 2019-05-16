import math
# Meet with math

# calculate square of halfsphere
pi = math.pi
radius_in_cm = 50

def half_square(pi, radius_in_cm):
    halfsquare_in_cm2 = (4 * pi * math.pow(radius_in_cm, 2)) / 2
    halfsquare_in_m2 = halfsquare_in_cm2 / 10000
    print('Halfsquare of sphere in m2: ', round(halfsquare_in_m2, 4))
    return round(halfsquare_in_m2, 4)

# show fraction and integer components of value
# first way
print('Fraction and integer components of value (first way): ', math.modf(half_square(pi, radius_in_cm)))
# second way
def fraction_integer(value):
    print('Fraction and integer components of value (second way): ', end='')
    return math.modf(value)

print(fraction_integer(half_square(pi, radius_in_cm)))

