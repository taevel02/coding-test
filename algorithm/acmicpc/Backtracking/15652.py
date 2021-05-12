n, m = map(int, input().split())
out = []
num = [i for i in range(1, n + 1)]


def solve(depth, n, m, start):
    if depth == m:
        print(*out)
        return

    for i in range(start, n + 1):
        out.append(i)
        solve(depth + 1, n, m, num[i - 1])
        out.pop()


solve(0, n, m, num[0])
