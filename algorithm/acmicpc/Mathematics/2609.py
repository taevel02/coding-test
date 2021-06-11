# 최대 공약수를 구하는 함수
def gcd(n, m):
    if m:
        return gcd(m, n % m)
    return n


n, m = map(int, input().split())
g = gcd(n, m)
print(int(g))
# 최소 공약수를 구하는 식: 두 수 곱한 후 최대공약수로 나누기
print(int((n * m) // g))
