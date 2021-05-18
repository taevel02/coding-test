from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
member = list(combinations(range(n), n//2))
ans = 100000

for m in member:
    a = set(m)
    b = list(set(range(n)) - a)
    a = list(a)

    a_teamwork, b_teamwork = 0, 0

    for i in range(n // 2 - 1):
        for j in range(i + 1, n // 2):
            a_teamwork += s[a[i]][a[j]] + s[a[j]][a[i]]
            b_teamwork += s[b[i]][b[j]] + s[b[j]][b[i]]

    ans = min(ans, abs(a_teamwork - b_teamwork))

print(ans)
