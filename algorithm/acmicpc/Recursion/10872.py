def sol(n):
    if n == 1 or n == 0:
        return 1
    return n * sol(n - 1)


print(sol(int(input())))
