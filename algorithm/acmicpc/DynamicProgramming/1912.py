n = int(input())
w = list(map(int, input().split()))
dp = [w[0]]

for i in range(len(w) - 1):
    dp.append(max(dp[i] + w[i+1], w[i+1]))

print(max(dp))
