n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i, j in sorted(data):
    print(i, j)
