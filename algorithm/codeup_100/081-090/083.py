h, b, c, s = list(map(int, input().split()))
storage = h*b*c*s   # bit
mb = storage / 8 / 2**10 / 2**10
print(round(mb, 1), "MB")
