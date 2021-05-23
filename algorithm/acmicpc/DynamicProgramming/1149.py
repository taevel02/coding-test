n = int(input())
dp = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    temp = list(map(int, input().split()))
    if i == 0:
        dp[0] = temp
    else:
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + temp[0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + temp[1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + temp[2]

print(min(dp[n-1]))
