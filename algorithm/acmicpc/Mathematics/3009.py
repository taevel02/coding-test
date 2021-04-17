lx = []
ly = []
for _ in range(3):
    x, y = map(int, input().split())

    if x in lx:
        lx.remove(x)
    else:
        lx.append(x)

    if y in ly:
        ly.remove(y)
    else:
        ly.append(y)

print(lx[0], ly[0])
