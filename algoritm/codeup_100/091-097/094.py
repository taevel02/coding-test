arr = [[0] * 19 for _ in range(19)]
n = int(input())

for _ in range(n):
    x, y = list(map(int, input().split()))
    arr[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(arr[i][j], end=' ')
    print()
