from collections import Counter

for _ in range(int(input())):
    n = int(input())
    s = []

    for _ in range(n):
        a, b = map(str, input().split())
        s.append(b)

    num = 1
    result = Counter(s)

    for i in result:
        num *= result[i] + 1

    print(num - 1)
