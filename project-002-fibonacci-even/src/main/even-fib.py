def even_fib (maximum):
    first = 1
    second = 1
    count = 1
    sum = 0

    while second < maximum:
        if count == 2:
            sum += second
            count = 0
        else:
            count += 1

        temp = second + first
        first = second
        second = temp

    return sum


print(even_fib(4000000))
