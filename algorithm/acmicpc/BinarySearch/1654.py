k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

low, high = 0, 10000000000
while low <= high:
    mid = (low + high) // 2
    num = 0
    for i in lans:
        num += i // mid
    if num >= n:
        low = mid + 1
    else:
        high = mid - 1

print(high)
