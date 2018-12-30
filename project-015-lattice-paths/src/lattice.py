#
# returns the number of unique lattice paths through a grid of width x and height y
#
def lattice(n):

    return factorial(n + 1, 2 * n) / factorial(1, n)



def factorial(bottom, n):
    retval = 1
    for x in range(bottom, n+1):
        retval *= x
    return retval