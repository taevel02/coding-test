def gcp(n, m):
    if m:
        return gcp(m, n % m)
    return n


for _ in range(int(input())):
    n, m = map(int, input().split())
    print(int((n * m) // gcp(n, m)))
