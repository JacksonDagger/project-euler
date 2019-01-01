def maxsum(fname):
    f = open(fname, "r")
    if f.mode == 'r':
        flines = f.readlines()
        linelist = []

        for x in flines:
            stringlist = x.split(" ")
            intlist = []
            for y in stringlist:
                intlist.append(int(y))
            linelist.append(intlist)

        line = len(flines)-2
        while line >= 0:
            for x in range(len(linelist[line])):
                temp = linelist[line][x]
                temp += max(linelist[line + 1][x], linelist[line + 1][x+1])
                linelist[line][x] = temp

            line -= 1
    else:
        return -1
    return linelist[0][0]
