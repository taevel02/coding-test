def counts(n):
    answer2 = 0
    answer5 = 0

    count = 1
    while True:
        if n // (2**count) > 0:
            answer2 += n // (2**count)
            count += 1
        else:
            break

    count = 1
    while True:
        if n // (5**count) > 0:
            answer5 += n // (5**count)
            count += 1
        else:
            break

    return answer2, answer5


n, m = map(int, input().split())
a1, b1 = counts(n)
a2, b2 = counts(m)
a3, b3 = counts(n - m)

print(min(a1 - a2 - a3, b1 - b2 - b3))
