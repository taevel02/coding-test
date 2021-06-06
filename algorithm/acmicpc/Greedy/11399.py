n = int(input())
p = list(map(int, input().split()))
p.sort()

time = 0
for i in range(n):
    for j in range(i+1):
        time += p[j]

print(time)
