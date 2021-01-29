w, h, b = list(map(int, input().split()))
storage = w*h*b
mb = storage / 8 / 2**10 / 2**10
print("%.2f MB" % mb)
