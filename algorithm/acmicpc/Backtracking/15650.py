n, m = map(int, input().split())
visited = [False]*n
out = []
result = []


def solve(depth, n, m):
    if depth == m:
        out_str = ' '.join(map(str, sorted(out)))
        if out_str not in result:
            result.append(out_str)
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            out.append(i + 1)
            solve(depth + 1, n, m)
            visited[i] = False
            out.pop()


solve(0, n, m)

for i in result:
    print(i)
