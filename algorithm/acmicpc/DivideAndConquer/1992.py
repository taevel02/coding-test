n = int(input())
image = [list(map(int, input().rstrip())) for _ in range(n)]
res = ''


def check(i, j, d):
    std = image[i][j]
    for x in range(i, i+d):
        for y in range(j, j+d):
            if image[x][y] != std:
                return -1
    return std


def solve(i, j, d):
    global res

    if d == 1:
        res += str(image[i][j])
        return

    chk = check(i, j, d)
    if chk == -1:
        res += '('
        d //= 2
        for p in range(2):
            for q in range(2):
                solve(i+p*d, j+q*d, d)
        res += ')'
    else:
        res += str(chk)
    return


solve(0, 0, n)
print(res)
