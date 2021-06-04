n, k = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))
data.sort(reverse=True)

i = 0
count = 0
while k != 0:
    if k >= data[i]:
        k -= data[i]
        count += 1
    else:
        i += 1

print(count)
