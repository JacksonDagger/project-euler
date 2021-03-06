#
# returns the smallest triangle number with more than numdiv integer divisors
#
def triangle_divisors(numdiv):
    n = 0
    trinum = 0
    while True:
        if get_num_divisors(trinum) > numdiv:
            return trinum
        n += 1
        trinum += n


#
# returns the nth triangle number
#
def triangle_number(n):
    if n % 2 == 0:
        return n / 2 * (n + 1)
    return (n / 2 + 1) * n


#
# returns the number of integer divisors of dividend
#
def get_num_divisors(dividend):
    n = 1
    numdiv = 0
    max = dividend

    while n < max:
        if dividend % n == 0:
            numdiv += 2
            max = dividend / n
            if n == max:
                numdiv -= 1
        n += 1

    return numdiv
