m = list(input())
n = list(input())
m_len = len(m)
n_len = len(n)

dp = [[0]*(n_len + 1) for _ in range(m_len + 1)]
for i in range(m_len):
    for j in range(n_len):
        if m[i] == n[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[m_len][n_len])
