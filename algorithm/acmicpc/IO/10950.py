n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append(a + b)

for i in range(n):
    print(arr[i])
