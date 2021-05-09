n, m = map(int, input().split())
visited = [False]*n
out = []


def solve(depth, n, m):
    if depth == m:
        print(*out)
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            out.append(i + 1)
            solve(depth + 1, n, m)
            visited[i] = False
            out.pop()


solve(0, n, m)
