from collections import Counter

n = int(input())
datan = list(map(int, input().split()))

m = int(input())
datam = list(map(int, input().split()))

counter = Counter(datan)

for i in datam:
    print(counter[i], end=' ')
