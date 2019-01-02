def namescore(fname):
    f = open(fname, "r")

    scoresum = 0

    if f.mode == 'r':
        names = f.read()
        origlist = names.split('"')
        namelist = []

        for x in origlist:
            if x != ',' and x != '':
                namelist.append(x)

        namelist.sort()

        for x in range(len(namelist)):
            scoresum += (x+1) * get_score(namelist[x])

    return scoresum


def get_score(instring):
    letternum = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26
    }
    scoresum = 0
    workstring = instring.upper()

    for x in workstring:
        scoresum += letternum.get(x)

    return scoresum





print(namescore("names.txt"))

