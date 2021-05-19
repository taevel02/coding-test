zero_dp = [1, 0, 1] + [0 for _ in range(38)]
one_dp = [0, 1, 1] + [0 for _ in range(38)]

for i in range(3, 41):
    zero_dp[i] = zero_dp[i-1] + zero_dp[i-2]
    one_dp[i] = one_dp[i-1] + one_dp[i-2]

for _ in range(int(input())):
    n = int(input())
    print(zero_dp[n], one_dp[n])
