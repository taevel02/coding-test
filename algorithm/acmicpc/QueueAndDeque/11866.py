from collections import deque

n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])

print('<', end='')
while q:
    for _ in range(k-1):
        q.append(q[0])
        q.popleft()
    print(q.popleft(), end='')

    if q:
        print(', ', end='')
print('>')
