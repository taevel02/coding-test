n = int(input())

dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i-1][j]
        elif i == j:
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    k += 1

print(max(dp[n-1]))
