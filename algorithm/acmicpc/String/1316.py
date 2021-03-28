n = int(input())
count = n

for _ in range(n):
    data = input()
    checker = []

    for i in range(len(data)):
        if (data[i] in checker) and (data[i] != checker[-1]):
            count -= 1
            break
        else:
            checker.append(data[i])

print(count)
