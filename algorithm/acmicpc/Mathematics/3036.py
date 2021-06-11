import math

n = int(input())
data = list(map(int, input().split()))

for i in range(1, n):
    gcd = math.gcd(data[0], data[i])
    print(f'{data[0] // gcd}/{data[i] // gcd}')
