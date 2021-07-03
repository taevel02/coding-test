p = 1000000007


def power(a, b):
    if b == 0:
        return 1
    if b % 2:
        return (power(a, b//2) ** 2 * a) % p
    else:
        return (power(a, b//2) ** 2) % p


n, k = map(int, input().split())
fact = [1 for _ in range(n+1)]

for i in range(2, n+1):
    fact[i] = fact[i-1] * i % p

A = fact[n]
B = (fact[n-k] * fact[k]) % p

# (A/B) % p
# = A * B^-1 % p
# = A * B^-1 * B^p-1 % p
# = A * B^p-2 % p
# = (A % p) * (B^p-2 % p) % p
print((A % p) * (power(B, p-2) % p) % p)
