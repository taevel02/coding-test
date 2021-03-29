a, b, c = map(int, input().split())
bp = 1

while a >= (c - b) * bp:
    if b >= c:
        bp = -1
        break
    bp += 1

print(bp)
