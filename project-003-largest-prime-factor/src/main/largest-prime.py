#
# generates the largest prime factor of the input
# @input: is a positive integer
#

def largest(input):
    testnum = 1
    upperbound = input
    largestPrime = 1

    while testnum<upperbound:
        if input % testnum == 0:
            upperbound = input / testnum
            prime = True
            for x in range(testnum/2):
                if testnum % (x+2) == 0:
                    prime = False
                    break
            if prime:
                largestPrime = testnum
        testnum += 1

    return largestPrime

print(largest(600851475143))