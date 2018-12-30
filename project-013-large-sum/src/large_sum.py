#
# returns the first ten digits of the sum of the hundred 50 digit numbers
#
def large_sum(fname):
    f = open(fname, "r")
    flines = f.readlines()
    intlines = []
    retval = 0

    for x in flines:
        intlines.append(int(x[:12]))
    for x in intlines:
        retval += x

    retstring = str(retval)

    return int(retstring[:10])


print(large_sum("challenge.txt"))
