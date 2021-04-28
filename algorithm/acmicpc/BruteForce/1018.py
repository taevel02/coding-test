start_black = []
start_white = []

ans = 100000

for i in range(8):
    if i % 2 == 0:
        start_black.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])
        start_white.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])
    else:
        start_black.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])
        start_white.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])


def test(x, y):
    corrent_b = 0
    corrent_w = 0

    for_compare = []
    if 0 <= x + 8 <= n and 0 <= y + 8 <= m:
        for i in range(x, x + 8):
            temp = []
            for j in range(y, y + 8):
                temp.append(chess[i][j])
            for_compare.append(temp)

        for i in range(8):
            for j in range(8):
                if for_compare[i][j] != start_black[i][j]:
                    corrent_b += 1

        for i in range(8):
            for j in range(8):
                if for_compare[i][j] != start_white[i][j]:
                    corrent_w += 1

        return min(corrent_b, corrent_w)

    return -1


n, m = map(int, input().split())
chess = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        res = test(i, j)
        if res != -1:
            if res < ans:
                ans = res

print(ans)
