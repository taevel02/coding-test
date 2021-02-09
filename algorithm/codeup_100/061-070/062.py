a, b, c = list(map(int, input().split()))
print((a if a < b else b) < c and (a if a < b else b) or c)
