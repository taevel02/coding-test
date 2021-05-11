n, m = map(int, input().split())
out = []


def solve(depth, n, m):
    if depth == m:
        print(*out)
        return

    for i in range(n):
        out.append(i + 1)
        solve(depth + 1, n, m)
        out.pop()


solve(0, n, m)
