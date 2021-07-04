n1, m1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n1)]

n2, m2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(n2)]

result = [[0]*m2 for _ in range(n1)]
for i in range(n1):
    for j in range(m2):
        for k in range(n2):
            result[i][j] = result[i][j] + A[i][k] * B[k][j]

for i in result:
    print(*i)
