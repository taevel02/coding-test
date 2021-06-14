import sys


def push(x):
    stack.append(x)


def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()


def size():
    return len(stack)


def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0


def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[len(stack) - 1]


stack = []
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()
    m = command[0]

    if m == 'push':
        push(command[1])
    elif m == 'pop':
        print(pop())
    elif m == 'size':
        print(size())
    elif m == 'empty':
        print(empty())
    elif m == 'top':
        print(top())
