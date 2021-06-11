def gcd(n, m):
    if m:
        return gcd(m, n % m)
    return n


for _ in range(int(input())):
    n, m = map(int, input().split())
    print(int((n * m) // gcd(n, m)))
