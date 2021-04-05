from math import comb

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    d = 0

    if k == 1:
        for i in range(1, n + 1):
            d += i
        print(d)
        continue
    else:
        d = 1
        for i in range(1, n):
            d += comb(k + i, i)
        print(d)
        continue
