while True:
    data = list(map(int, input().split()))
    if data[0] == data[1] == data[2] == 0:
        break

    data = sorted(data)

    if data[0] ** 2 + data[1] ** 2 == data[2] ** 2:
        print('right')
    else:
        print('wrong')
