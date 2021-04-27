n = int(input())
datax = []
datay = []

rank = []

for _ in range(n):
    x, y = map(int, input().split())
    datax.append(x)
    datay.append(y)

for i in range(n):
    count = 1
    for j in range(n):
        if datax[i] < datax[j] and datay[i] < datay[j]:
            count += 1
    rank.append(count)

for i in rank:
    print(i)
