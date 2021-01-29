location = [[0] * 10 for _ in range(10)]

for i in range(10):
    data = list(map(int, input().split()))
    for j in range(10):
        location[i][j] = data[j]

x, y = 1, 1
while True:
    if location[x][y] == 0:
        location[x][y] = 9
    elif location[x][y] == 2:
        location[x][y] = 9
        break

    if (location[x][y+1] == 1 and location[x+1][y] == 1) or (x == 8 and y == 8):
        break

    if location[x][y+1] != 1:
        y += 1
    elif location[x+1][y] != 1:
        x += 1

for i in range(10):
    for j in range(10):
        print(location[i][j], end=' ')
    print()
