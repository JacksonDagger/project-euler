import math


def main():
    numlist = [1]
    for x in range(320):
        numlist.append(0)

    carry = 0
    for x in range(1, 1001):
        for y in range(0, 315):
            numlist[y] = numlist[y]*2
            numlist[y] = numlist[y]+carry
            carry = numlist[y]/10
            numlist[y] = numlist[y]-10*carry

    pdsum = 0
    for x in numlist:
        pdsum += x

    print(pdsum)




main()