def dfs(depth, now):
    global add, sub, mul, div, max_result, min_result

    if depth == n:
        max_result = max(max_result, now)
        min_result = min(min_result, now)

    else:
        if add > 0:
            add -= 1
            dfs(depth + 1, now + arr[depth])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(depth + 1, now - arr[depth])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(depth + 1, now * arr[depth])
            mul += 1
        if div > 0:
            div -= 1
            dfs(depth + 1, int(now / arr[depth]))
            div += 1


n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -1e9
min_result = 1e9

dfs(1, arr[0])
print(max_result)
print(min_result)
