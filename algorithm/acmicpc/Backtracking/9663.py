def solve(col):
    global count

    if col == n:
        count += 1
        return

    for i in range(n):
        if column[i] or right[col - i] or left[col + i]:
            continue
        column[i] = True
        right[col - i] = True
        left[col + i] = True
        solve(col + 1)
        column[i] = False
        right[col - i] = False
        left[col + i] = False


n = int(input())
count = 0

column = [False]*(n * 2 - 1)
right = [False]*(n * 2 - 1)
left = [False]*(n * 2 - 1)

solve(0)
print(count)
