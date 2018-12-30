#
# returns the length of the longest Collatz sequence starting at a number below n
#
def largest_collatz(n):
    maxlength = 0
    index = 0
    for x in range(n):
        temp = collatz_length(x)
        if temp > maxlength:
            maxlength = temp
            index = x
    return index


#
# returns the length of the Collatz sequence starting at n
#
def collatz_length(n):
    length = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3 * n + 1
        length += 1
    return length