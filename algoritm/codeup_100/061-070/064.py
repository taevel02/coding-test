data = list(map(int, input().split()))
for i in range(3):
    if data[i] % 2 == 0:
        print("even")
    else:
        print("odd")
