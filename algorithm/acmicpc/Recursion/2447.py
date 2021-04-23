ans = []
n = int(input())

for dy in range(n):
    for dx in range(n):
        flag = 1
        y = dy
        x = dx

        while y != 0:
            if y % 3 == 1 and x % 3 == 1:
                flag = 2
                ans.append(' ')
                break
            y //= 3
            x //= 3

        if flag == 1:
            ans.append('*')
    ans.append('\n')

result = ''.join(ans)
print(result)
