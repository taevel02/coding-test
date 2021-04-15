arr = [False, False] + [True] * 9999
for i in range(2, 101):
    if arr[i]:
        for j in range(i * 2, len(arr), i):
            arr[j] = False

for _ in range(int(input())):
    n = int(input())
    temp = int(n // 2)
    for i in range(n // 2 + 1):
        if arr[temp] and arr[n - temp]:
            print(f'{temp} {n - temp}')
            break
        temp -= 1
