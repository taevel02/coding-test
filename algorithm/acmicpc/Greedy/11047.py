n, k = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))
data.sort(reverse=True)

count = 0
for i in range(n):
    if k == 0:
        break
    if data[i] <= k:
        count += k // data[i]
        k %= data[i]

print(count)
