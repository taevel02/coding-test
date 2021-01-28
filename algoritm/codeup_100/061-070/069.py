data = list(map(int, input().split()))
for i in range(len(data)):
    if data[i] != 0:
        print(data[i])
    else:
        break
