#
# Takes a number of digits and returns the largest palindromic number that can be made from a number of length first
# multiplied with a number of length second
# first, second: the digit lengths >0
#


def palindrome_factor(first, second):
    max1 = 1
    for x in range(first):
        max1 *= 10
    max1 -= 1

    max2 = 1
    for x in range(second):
        max2 *= 10
    max2 -= 1

    largest = 0


    while (max1 > 0):
        secondnum = max2
        while(secondnum > 0):
            test = max1 * secondnum
            if is_palindrome(test) and test > largest:
                largest = test
            secondnum -= 1
        max1 -= 1

    return largest


#
# Takes an integer and returns true if it is a palindrome and false otherwise. Negative signs are ignored
#

def is_palindrome(input):
    numList = []

    while input > 0:
        mod = input % 10
        numList.append(mod)
        input -= mod
        input /= 10

    forward = []
    forward.extend(numList)

    numList.reverse()

    return numList == forward
