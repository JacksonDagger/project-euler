#
# generates the sum of all integers that are a multiple of 3 or 5 between 0 and the inputted max
# @max: is a positive integer greater th


def euler1(maximum):
    sum = 0
    prod3 = 0
    prod5 = 0
    while prod3 < maximum or prod5 < maximum:
        if prod5 > prod3:
            prod3 += 3
            if prod3 < maximum and not(prod5 == prod3):
                sum += prod3

        else:
            prod5 += 5
            if prod5 < 1000:
                sum += prod5

    return sum


print (euler1(1000))