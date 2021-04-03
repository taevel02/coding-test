import math

a, b, v = map(int, input().split())
d = (v - a) / (a - b)
print(math.ceil(d) + 1)
