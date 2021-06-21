import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([])

for _ in range(n):
    command = sys.stdin.readline().split()
    m = command[0]

    if m == 'push_front':
        q.appendleft(command[1])
    elif m == 'push_back':
        q.append(command[1])
    elif m == 'pop_front':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif m == 'pop_back':
        if len(q):
            print(q.pop())
        else:
            print(-1)
    elif m == 'size':
        print(len(q))
    elif m == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif m == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif m == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)
