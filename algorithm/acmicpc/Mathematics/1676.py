from math import factorial

n = int(input())
fac = list(str(factorial(n)))

new_fac = []
for i in range(len(fac) - 1, -1, -1):
    new_fac.append(fac[i])

result = 0
for i in range(len(new_fac)):
    if new_fac[i] != '0':
        result = i
        break

print(result)
