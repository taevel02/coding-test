from collections import Counter

n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

print(round(sum(data) / n))
print(sorted(data)[n // 2])

data.sort()
modes = Counter(data).most_common()
if len(data) > 1:
    if modes[0][1] == modes[1][1]:
        print(modes[1][0])
    else:
        print(modes[0][0])
else:
    print(modes[0][0])

print(max(data) - min(data))
