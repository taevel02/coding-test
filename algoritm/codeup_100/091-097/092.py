n = int(input())
array = []
data = list(map(int, input().split()))

for i in range(n):
    array.append(int(data[i]))

i = n-1
while i >= 0:
    print(array[i], end=' ')
    i -= 1
