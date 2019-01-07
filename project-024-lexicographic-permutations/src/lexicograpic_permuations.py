def getlexperms(inlist):
    if len(inlist) <= 1:
        return [inlist]
    inlist.sort()
    retlist = []
    for x in inlist:
        passlist = []
        passlist.extend(inlist)
        passlist.remove(x)
        tempret = getlexperms(passlist)
        for y in tempret:
            tempadd = [x]
            tempadd.extend(y)
            retlist.append(tempadd)

    return retlist




print((getlexperms([0,1,2, 3, 4, 5, 6, 7, 8, 9])[999999]))
