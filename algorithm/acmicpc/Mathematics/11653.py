def sol(n):
    data = []

    i = 2
    while i * i <= n:
        if n % i == 0:
            data.append(i)
            n //= i
        else:
            i += 1

    if n != 1:
        data.append(n)

    return data


for i in sol(int(input())):
    print(i)
