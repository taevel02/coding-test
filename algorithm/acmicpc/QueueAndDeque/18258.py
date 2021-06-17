import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([])

for _ in range(n):
    command = sys.stdin.readline().split()
    m = command[0]

    if m == 'push':
        q.append(command[1])
    elif m == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif m == 'size':
        print(len(q))
    elif m == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif m == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif m == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
