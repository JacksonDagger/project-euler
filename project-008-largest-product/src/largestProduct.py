def largestProduct(length, digits):
    stringlist = list(digits)

    intlist = []
    for x in stringlist:
        intlist.append(int(x))
    maximum = 0
    index = 0
    listlength = len(intlist)

    while index + length < listlength:
        temp = 1
        for x in range(length):
            temp *= intlist[index + x]

        if temp > maximum:
            maximum = temp

        index += 1

    return maximum