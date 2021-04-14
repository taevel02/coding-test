def sol(n):
    arr = [False, False] + [True] * 2 * n
    for i in range(2, int((2 * n) ** 0.5) + 1):
        if arr[i]:
            for j in range(i * 2, len(arr), i):
                arr[j] = False

    return [i for i in range(n + 1, 2 * n + 1) if arr[i]]


while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(len(sol(n)))
