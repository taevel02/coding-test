def sol(n):
    if n == 1:
        return 1
    return n * sol(n - 1)


print(sol(int(input())))
