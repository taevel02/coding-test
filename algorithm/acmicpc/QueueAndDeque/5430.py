# from collections import deque


# def r():
#     if len(s):
#         s.reverse()
#     else:
#         return False


# def d():
#     if len(s):
#         s.popleft()
#     else:
#         return False


# for _ in range(int(input())):
#     p = input()
#     n = int(input())
#     s = input()
#     s = deque(''.join(i for i in s if i not in '[],'))

#     for i in p:
#         if i == 'R':
#             r()
#         elif i == 'D':
#             d()

#     if len(s):
#         s = ','.join(s)
#         print('[', end='')
#         print(s, end='')
#         print(']')
#     else:
#         print('error')

import sys
from collections import deque

for _ in range(int(input())):
    p = sys.stdin.readline()
    n = int(input())
    s = sys.stdin.readline()

    flag = 1
    try:
        if n == 0:
            s = []
        else:
            s = deque(list(map(int, s.strip()[1:-1].split(','))))

        for i in p:
            if i == 'R':
                flag *= -1
            elif i == 'D':
                if s:
                    if flag == 1:
                        s.popleft()
                    else:
                        s.pop()
                else:
                    raise ValueError
    except ValueError:
        print('error')
    else:
        if flag == -1:
            s = reversed(s)
        print('[' + ','.join(list(map(str, s))) + ']')
