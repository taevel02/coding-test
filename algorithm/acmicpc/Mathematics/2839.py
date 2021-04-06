n = int(input())
count = 0

while n != 0:
    if n % 5 == 0:
        count += 1
        n -= 5
        continue
    elif n % 3 == 0:
        count += 1
        n -= 3
        continue
    elif n > 5:
        count += 1
        n -= 5
        continue
    elif n > 3:
        count += 1
        n -= 3
        continue

    if n % 5 != 0 and n % 3 != 0:
        count = -1
        break

print(count)
