from collections import deque

n, m = map(int, input().split())
s = deque(map(int, input().split()))

q = deque([i for i in range(1, n+1)])
count = 0

while len(s):
    t = s.popleft()
    t_point = q.index(t)

    if t_point != 0:
        if len(q) - t_point > t_point:
            q.rotate(-t_point)
            count += t_point
        else:
            q.rotate(len(q) - t_point)
            count += len(q) - t_point

    q.popleft()

print(count)
