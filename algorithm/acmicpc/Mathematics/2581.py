def primeNum(n):
    arr = [2] + list(range(3, n + 1, 2))

    i = 1
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[j] % arr[i] == 0:
                arr.pop(j)
            else:
                j += 1
        i += 1

    return arr


m = int(input())
n = int(input())
data = []

for i in primeNum(n):
    if m <= i <= n:
        data.append(i)

if len(data) == 0:
    print(-1)
else:
    print(sum(data))
    print(data[0])
