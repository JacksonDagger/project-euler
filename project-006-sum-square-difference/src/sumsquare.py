#
# Returns the difference between the square of the sum of the first max natural numbers
# and the sum of the squares of the first max natural number
#


def sumsquareddiff(max):
    sum_of_squares=0
    for x in range(max):
        sum_of_squares += (x+1) * (x+1)

    sum = 0
    for x in range(max):
        sum += (x+1)

    square_of_sums = sum * sum

    return square_of_sums - sum_of_squares
