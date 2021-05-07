n = int(input())

data = []
for i in range(n):
    a, b = map(str, input().split())
    data.append([format(i, '06'), format(int(a), '03'), b])

data.sort(key=lambda x: (x[1], x[0]))
for i, j, k in data:
    print(int(j), k)
