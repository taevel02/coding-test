n = int(input())
data = list(map(int, input().split()))
data.sort()

m = int(input())
data2 = list(map(int, input().split()))

for i in range(m):
    x = data2[i]
    start = 0
    end = n - 1
    flag = False

    while start <= end:
        mid = (start + end) // 2
        if data[mid] < x:
            start = mid + 1
        elif data[mid] > x:
            end = mid - 1
        else:
            flag = True
            break

    print(int(flag))
