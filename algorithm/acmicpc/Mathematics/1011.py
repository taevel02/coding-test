t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    r = (y - x) / 2
    k = 1

    while r > k:
        r -= k
        k += 1

    if r * 2 <= k:
        k = k * 2 - 1
    else:
        k *= 2

    print(k)
