import sys

k = int(sys.stdin.readline())
stack = []

for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
