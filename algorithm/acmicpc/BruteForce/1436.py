n = int(input())
cnt = 666
temp = cnt

while True:
    if n == 1:
        break
    cnt += 1
    if str(cnt).count('666') >= 1:
        temp = cnt
        n -= 1

print(temp)
