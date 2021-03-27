import sys
t = int(sys.stdin.readline())
s = [['0']*t for _ in range(t)]

for i in range(t):
    data = list(map(str, sys.stdin.readline().split()))
    for j in range(2):
        s[i][j] = data[j]
        s[i][j] = data[j]

for i in range(t):
    for j in s[i][1]:
        for _ in range(int(s[i][0])):
            print(j, end='')
    print()
