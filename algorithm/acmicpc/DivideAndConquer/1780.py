n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
zero, pone, mone = 0, 0, 0


def check(i, j, d):
    global zero, pone, mone
    std = paper[i][j]

    for x in range(i, i+d):
        for y in range(j, j+d):
            if paper[x][y] != std:
                d //= 3
                check(i, j, d)
                check(i, j+d, d)
                check(i, j+(2*d), d)
                check(i+d, j, d)
                check(i+d, j+d, d)
                check(i+d, j+(2*d), d)
                check(i+(2*d), j, d)
                check(i+(2*d), j+d, d)
                check(i+(2*d), j+(2*d), d)
                return

    if std == -1:
        mone += 1
    elif std == 0:
        zero += 1
    elif std == 1:
        pone += 1
    return


check(0, 0, n)
print(mone)
print(zero)
print(pone)
