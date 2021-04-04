t = int(input())
data = ['' for _ in range(t)]

for i in range(t):
    h, w, n = map(int, input().split())
    data[i] = str((n - 1) % h + 1) + str((n - 1) // h + 1).rjust(2, '0')

for i in data:
    print(i)
