#
# Returns the nth prime number
# n is an integer greater than 0
#


def getnthprime(n):
    primelist = [2]
    nextnum = 3

    while len(primelist) < n:
        prime = True

        for x in primelist:
            if nextnum % x == 0:
                prime = False
                break

        if prime:
            primelist.append(nextnum)
        nextnum += 1

    return primelist[n-1]