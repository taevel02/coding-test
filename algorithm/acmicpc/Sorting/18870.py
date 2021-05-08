n = int(input())
data = list(map(int, input().split()))
data2 = sorted(set(data))

dic = {data2[i]: i for i in range(len(data2))}
print(*[dic[i] for i in data])
