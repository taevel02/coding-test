a, r, n = list(map(int, input().split()))
result = a
for i in range(n-1):
    result *= r
print(result)
