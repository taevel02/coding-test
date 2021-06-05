n = int(input())
data = []

for i in range(n):
    start, end = map(int, input().split())
    data.append([start, end])

data.sort(key=lambda x: x[0])
data.sort(key=lambda x: x[1])

last = 0
count = 0
for i, j in data:
    if i >= last:
        count += 1
        last = j

print(count)
