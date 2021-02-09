arr = []
t = int(input())

for _ in range(t):
    a, b = map(int, input().split(','))
    arr.append(a + b)

for i in arr:
    print(i)
