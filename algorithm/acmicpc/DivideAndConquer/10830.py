def time(a, b):
    temp = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += a[i][k] * b[k][j]
            temp[i][j] %= 1000

    return temp


def solve(a, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000
        return a

    temp = solve(a, b//2)

    if b % 2 == 0:
        return time(temp, temp)
    else:
        return time(time(temp, temp), a)


n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = solve(matrix, b)
for ans in result:
    print(*ans)
