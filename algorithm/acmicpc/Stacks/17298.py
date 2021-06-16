n = int(input())
s = list(map(int, input().split()))

stack = []
nge = [-1 for _ in range(n)]

stack.append(0)
i = 1

while stack and i < n:
    while stack and s[stack[-1]] < s[i]:
        nge[stack[-1]] = s[i]
        stack.pop()
    stack.append(i)
    i += 1

print(*nge)
