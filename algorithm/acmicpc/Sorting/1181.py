n = int(input())

data = []
for _ in range(n):
    char = input()
    if char not in data:
        data.append(char)

data.sort(key=lambda x: (len(x), x))
for i in data:
    print(i)
