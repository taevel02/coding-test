def sol(n):
    n -= 1
    m = 6
    count = 1

    while n > 0:
        n -= m
        m += 6
        count += 1

    return count


print(sol(int(input())))
