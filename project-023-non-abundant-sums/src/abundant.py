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
def dfunc(n):
    sumlist = get_divisors(n)

    dsum = 0

    for x in sumlist:
        dsum += x
    dsum -= n
    return dsum


#
# returns the sum of all numbers that cannot be made from the sum of two abundant numbers
#
def sum_non_abundant_sum():
    abnums = generate_abundant_numbers(28123)
    retval = 0


    possiblenums = range(28123)

    for x in abnums:
        for y in abnums:
            if x + y in possiblenums:
                possiblenums.remove(x + y)

    for x in possiblenums:
        retval += x

    return retval


print(sum_non_abundant_sum())