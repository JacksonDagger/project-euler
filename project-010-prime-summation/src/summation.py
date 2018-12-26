#
# returns the sum of all primes below n
# n is an integer >2
#


def getprimesumbelow(n):
    primelist = [2]
    nextnum = 3

    while  nextnum < n:
        prime = True

        for x in primelist:
            if nextnum % x == 0:
                prime = False
                break

        if prime:
            primelist.append(nextnum)
        nextnum += 1

    sum = 0
    for x in primelist:
        sum += x

    return sum