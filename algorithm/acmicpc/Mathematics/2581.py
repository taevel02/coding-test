def sol(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


m = int(input())
n = int(input())
data = []

for i in range(m, n + 1):
    if sol(i):
        data.append(i)

if len(data) == 0:
    print(-1)
else:
    print(sum(data))
    print(sorted(data)[0])
