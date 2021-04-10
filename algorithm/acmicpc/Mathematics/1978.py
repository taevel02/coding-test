def sol(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


n = int(input())
data = list(map(int, input().split()))
count = 0

for i in range(n):
    if sol(data[i]):
        count += 1

print(count)
