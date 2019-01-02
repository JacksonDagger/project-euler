#
# returns a lsit of proper divisors of dividend. Code is heavily borrowed from get_num_divisors in proj 12
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
# returns d(n)
#
def dfunc(n):
    sumlist = get_divisors(n)

    dsum = 0

    for x in sumlist:
        dsum += x
    dsum -= n
    return dsum


#
# sums all amicable numbers under n
#
def amicable_sum(n):
    asum = 0
    for x in range(2, n):
        y = dfunc(x)
        if dfunc(y) == x and y != x:
            asum += x
    return asum
