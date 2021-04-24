def hanoi(n, a, b):
    if n == 0:
        return 0

    hanoi(n - 1, a, 6 - a - b)
    print(f'{a} {b}')
    hanoi(n - 1, 6 - a - b, b)


n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 3)
