arr = [False, False] + [True] * 999999
for i in range(2, 1001):
    if arr[i]:
        for j in range(i * 2, len(arr), i):
            arr[j] = False

m, n = map(int, input().split())
nums = [i for i in range(m, n + 1) if arr[i]]
for i in nums:
    print(i)
