primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

#
#Outputs the smallest number that is a multiple of input and all positive integers less than input
#

def smallest_multiple(input):
    retval = 1
    mainlist = []

    for x in range(input-2):
        mainlist.append(x+2)

    for x in primes:
        max = 0
        for y in mainlist:
            tempList = prime_factorize(y)
            temp = tempList.count(x)
            if temp > max:
                max = temp
        for y in range(max):
            retval *= x
    return retval


def prime_factorize(input):
    retlist = []
    if input == 1:
        return retlist

    for x in primes:
        if input % x == 0:
            retlist.append(x)
            retlist.extend(prime_factorize(input / x))
            break
    return retlist
