import sys

inf = sys.maxsize

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    file_sizes = list(map(int, sys.stdin.readline().split()))

    dp = [[0]*k for _ in range(k)]
    s = [sum(file_sizes[0:i+1]) for i in range(k)]

    for gap in range(1, k):
        for start in range(k - gap):
            end = start + gap
            dp[start][end] = inf
            for i in range(start, end):
                dp[start][end] = min(
                    dp[start][end], dp[start][i] + dp[i+1][end])
            dp[start][end] += s[end] - s[start-1] if start != 0 else s[end]

    print(dp[0][-1])
