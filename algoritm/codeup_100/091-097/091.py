n = int(input())
array = [0 for _ in range(23)]
data = list(map(int, input().split()))

for i in range(n):
    array[data[i]-1] += 1

for i in range(23):
    print(array[i], end=' ')
