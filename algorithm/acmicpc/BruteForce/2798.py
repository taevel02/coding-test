n, m = map(int, input().split())
data = list(map(int, input().split()))

temp = 0
sum_ = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or k == i:
                continue

            sum_ = data[i] + data[j] + data[k]
            if temp < sum_ and sum_ <= m:
                temp = sum_

print(temp)
