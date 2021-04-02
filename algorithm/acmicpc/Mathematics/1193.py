def sol(x):
    n = 1
    while x > n:
        x -= n
        n += 1

    return [
        str(x) + '/' + str(n - x + 1),
        str(n - x + 1) + '/' + str(x)
    ][n % 2]


print(sol(int(input())))
