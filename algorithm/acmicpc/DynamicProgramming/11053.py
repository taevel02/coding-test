n = int(input())
w = list(map(int, input().split()))

dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if w[i] > w[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
