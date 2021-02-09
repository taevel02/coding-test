n = int(input())
result = 0
i = 0
while True:
    i += 1
    result += i
    if result >= n:
        print(i)
        break
