arr = [[0] * 19 for _ in range(19)]

for i in range(19):
    data = list(map(int, input().split()))
    for j in range(19):
        arr[i][j] = data[j]

n = int(input())

for i in range(n):
    x, y = list(map(int, input().split()))
    for j in range(19):
        if arr[x-1][j] == 0:
            arr[x-1][j] = 1
        else:
            arr[x-1][j] = 0
        if arr[j][y-1] == 0:
            arr[j][y-1] = 1
        else:
            arr[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(arr[i][j], end=' ')
    print()
