n = int(input())

for i in range(n):
    for _ in range(n - i - 1):
        print(end=' ')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
