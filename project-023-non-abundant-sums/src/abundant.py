#
# returns d(n) = sum of divisors not equal to dividend. Borrowed from proj 21
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
# returns the sum of all numbers that cannot be made from the sum of two abundant numbers
#
def sum_non_abundant_sum():
    retsum = (28111*28111+28111)/2
    ablist = [12]
    for x in range(12, 28112):
        if ablist[-1] < x:
            for y in range(x, 28112):
                if dfunc(y) > y:
                    ablist.append(y)

        for ab in ablist:
            if x - ab in ablist:
                retsum -= x
                

    return retsum


print(sum_non_abundant_sum())

