from collections import Counter

n, m = map(int, input().split())
trees = list(map(int, input().split()))

data = Counter(trees)

low, high = 0, max(data)
result = 0
while low <= high:
    total = 0
    mid = (low + high) // 2

    for i, num in data.items():
        if i > mid:
            total += (i-mid)*num

    if total < m:
        high = mid - 1
    else:
        result = mid
        low = mid + 1

print(result)
