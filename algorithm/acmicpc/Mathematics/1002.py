for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    if d == 0 and r1 == r2:
        print(-1)
        continue

    if (d > r1 + r2) or (d + min(r1, r2) < max(r1, r2)):
        print(0)
    elif (d + min(r1, r2) == max(r1, r2)) or (d == r1 + r2):
        print(1)
    else:
        print(2)
