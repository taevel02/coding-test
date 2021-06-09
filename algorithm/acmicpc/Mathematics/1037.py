n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[0]*data[-1])
