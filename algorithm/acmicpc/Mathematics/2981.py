import math

n = int(input())
s = []
a = []
gcd = 0

for i in range(n):
    s.append(int(input()))
    if i == 1:
        gcd = abs(s[1] - s[0])
    gcd = math.gcd(abs(s[i] - s[i-1]), gcd)

gcd_a = int(gcd ** 0.5)
for i in range(2, gcd_a + 1):
    if gcd % i == 0:
        a.append(i)
        a.append(gcd // i)

a.append(gcd)
a = list(set(a))
a.sort()

print(*a)
