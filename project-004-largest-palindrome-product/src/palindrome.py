def palindrome_factor (first, second):

def is_palindrome(input):
    divisor = 10
    previous = 1
    numList = []

    while input > previous:
        mod = input % divisor
        numList.append(mod)
        previous = divisor
        divisor *= 10

    return numList==numList.reverse()
