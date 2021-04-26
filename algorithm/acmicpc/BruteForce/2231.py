def sol(n):
    temp = n
    for i in range(n):
        d = sum([int(j) for j in str(i)])
        if n == d + i and temp > i:
            temp = i

    if temp == n:
        return 0

    return temp


print(sol(int(input())))
