#
# returns the sum of the number of letters in each number from lower to upper inclusive
#
def nlsum(lower, upper):
    retval = 0
    for x in range(lower, upper + 1):
        retval += numletter(x)
    return retval
#
# returns the number of letters used in the british spelling of n. hyphens and spaces not included
#
def numletter(n):
    retval = 0


    if n == 1000:
        retval = 11
    else:
        if n < 0 or n > 1000:
            retval = -1
        if 0 <= n < 20:
            retval += get_under_twenty(n)
        else:
            if n < 100:
                retval += numletter(n % 10)
                tens = n // 10
                retval += get_tens(tens)
            else:
                retval += numletter(n // 100)
                retval += 7 #"hundred"
                if n % 100 != 0:
                    retval += 3 #"and"
                    retval += numletter(n % 100)

    return retval

def get_under_twenty(argument):
    switcher = {
        0: 0,
        1: 3,
        2: 3,
        3: 5,
        4: 4,
        5: 4,
        6: 3,
        7: 5,
        8: 5,
        9: 4,
        10: 3,
        11: 6,
        12: 6,
        13: 7,
        14: 8,
        15: 7,
        16: 7,
        17: 9,
        18: 9,
        19: 8
    }

    return switcher.get(argument)

def get_tens(argument):
    switcher = {
        2: 6,
        3: 6,
        4: 5,
        5: 5,
        6: 5,
        7: 7,
        8: 6,
        9: 6
    }

    return switcher.get(argument)
