n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0


def check(i, j, d):
    std = paper[i][j]
    for x in range(i, i+d):
        for y in range(j, j+d):
            if paper[x][y] != std:
                return False
    return True


def solve(i, j, d):
    global white, blue

    if check(i, j, d):
        if paper[i][j]:
            blue += 1
        else:
            white += 1
        return
    else:
        d //= 2
        solve(i, j, d)
        solve(i, j+d, d)
        solve(i+d, j, d)
        solve(i+d, j+d, d)
        return


solve(0, 0, n)
print(white)
print(blue)
