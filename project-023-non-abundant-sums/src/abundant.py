#
# generates a list of all abundant numbers less than n
#
def generate_abundant_numbers(n):
    abundantlist = []
    for x in range(12, n):
        if dfunc(x) > x:
            abundantlist.append(x)

    return abundantlist



#
# returns a lsit of proper divisors of dividend. Borrowed from proj 21
#
def get_divisors(dividend):
    n = 1
    divisors = []
    max = dividend

    while n < max:
        if dividend % n == 0:
            divisors.append(n)
            max = dividend / n
            if n != max:
                divisors.append(max)
        n += 1

    return divisors


#
# returns d(n). Borrowed from proj 21
#
def dfunc(dividend):
    n = 1
    dsum = 0
    max = dividend

    while n < max:
        if dividend % n == 0:
            dsum += n
            max = dividend / n
            if n != max:
                dsum += max
        n += 1

    return dsum - dividend

#
# returns true if n is abundant
#
def isabundant(n):
    return dfunc(n) > n


#
# returns the sum of all numbers that cannot be made from the sum of two abundant numbers
#
def sum_non_abundant_sum():
    ablist = generate_abundant_numbers(28111)
    ablen = len(ablist)
    nonabsum = range(28123)
    for x in range(ablen):
        for y in range(x, ablen):
            tempsum = ablist[x] + ablist[y]
            if tempsum > 28123:
                break
            if tempsum in nonabsum:
                nonabsum.remove(tempsum)
    retsum = 0
    for x in nonabsum:
        retsum += x
    return retsum

print(sum_non_abundant_sum())




