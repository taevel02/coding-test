t = int(input())
x = 0
y = 0
data = [0 for _ in range(t)]

for i in range(t):
    h, w, n = map(int, input().split())

    if h == 1:
        x = int(n / h)
        y = 1
    elif n % h == 0:
        x = int(n / h)
        y = h
    else:
        x = int(n / h + 1)
        y = int(n % h)

    if x < 10:
        data[i] = f'{y}0{x}'
    else:
        data[i] = f'{y}{x}'

for i in data:
    print(i)
