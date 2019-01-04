def fibonacci(numdig):
    index = 2
    fib0 = [1]
    fib1 = [1]
    digs = 1

    while digs < numdig:
        if index % 2 == 0:
            carry = 0
            for x in range(digs + 1):
                if x >= len(fib0):
                    if carry > 0:
                        if x < len(fib1):
                            fib0.append(0)
                            fib0[x] = fib0[x] + fib1[x] + carry
                            carry = fib0[x] // 10
                            fib0[x] = fib0[x] - 10 * carry
                        else:
                            fib0.append(carry)
                    else:
                        if x < len(fib1):
                            fib0.append(fib1[x])

                else:
                    fib0[x] = fib0[x] + fib1[x] + carry
                    carry = fib0[x]//10
                    fib0[x] = fib0[x] - 10 * carry
            digs = len(fib0)
        else:
            carry = 0
            for x in range(digs + 1):
                if x >= len(fib1):
                    if carry > 0:
                        if x < len(fib0):
                            fib1.append(0)
                            fib1[x] = fib1[x] + fib0[x] + carry
                            carry = fib1[x] // 10
                            fib1[x] = fib1[x] - 10 * carry
                        else:
                            fib1.append(carry)
                    else:
                        if x < len(fib0):
                            fib1.append(fib0[x])

                else:
                    fib1[x] = fib1[x] + fib0[x] + carry
                    carry = fib1[x]//10
                    fib1[x] = fib1[x] - 10 * carry
            digs = len(fib1)
        index += 1

    return index

print(fibonacci(1000))