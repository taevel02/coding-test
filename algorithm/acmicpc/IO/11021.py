arr = []
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    arr.append(a + b)

for i in range(len(arr)):
    print(f'Case #{i + 1}:', arr[i])
