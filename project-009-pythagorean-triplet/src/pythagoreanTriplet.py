import math

#
# Returns the product of the pythagorean triplet that sums to x or -1 if no such triplet exists
# x: an even integer > 0
#


def pyTrip(x):

    for y in range(x/3):
        a = y + 1
        for b in range (a, x - 2*a, 1):
            c = int(math.sqrt(a*a + b*b))
            if a + b + c == x:
                if c*c == a*a + b*b:
                    return a*b*c

    return -1
