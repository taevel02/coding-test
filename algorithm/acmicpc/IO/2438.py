n = int(input())

for i in range(n):
    for _ in range(-1, i):
        print('*', end='')
    print()
