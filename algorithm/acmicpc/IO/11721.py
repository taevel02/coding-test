import sys
v = sys.stdin.readline()
start = 0
end = 10

while True:
    if end < len(v):
        print(v[start:end])
        start += 10
        end += 10
    else:
        print(v[start:])
        break
