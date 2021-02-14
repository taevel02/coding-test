n = int(input())

for i in range(n - 1):
    print(' ' * (n - i - 1), end='')
    print('*', end=' ' * (2 * i - 1))
    if i != 0:
        print('*')
    else:
        print()
print('*' * (2 * n - 1))
