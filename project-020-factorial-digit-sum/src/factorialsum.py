def factsum(n):
    numlist = [1]
    for x in range(320):
        numlist.append(0)

    carry = 0
    for x in range(1, n+1):
        for y in range(0, 315):
            numlist[y] = numlist[y]*x
            numlist[y] = numlist[y]+carry
            carry = numlist[y]/10
            numlist[y] = numlist[y]-10*carry

    fdsum = 0
    for x in numlist:
        fdsum += x

    return(fdsum)

print(factsum(100))