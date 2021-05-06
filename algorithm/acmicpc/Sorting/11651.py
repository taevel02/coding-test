n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: (x[1], x[0]))
for i, j in data:
    print(i, j)
