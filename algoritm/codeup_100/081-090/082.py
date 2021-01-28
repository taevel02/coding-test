r, g, b = list(map(int, input().split()))
result = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            result += 1
print(result)
