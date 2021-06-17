import sys
import queue

n = int(sys.stdin.readline())
que = queue.Queue()


def push(x):
    que.put(x)


def pop():
    if que.qsize():
        return que.get()
    else:
        return -1


def size():
    return que.qsize()


def empty():
    if que.qsize():
        return 0
    else:
        return 1


def front():
    if que.qsize():
        return que.queue[0]
    else:
        return -1


def back():
    if que.qsize():
        return que.queue[-1]
    else:
        return -1


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
    elif m == 'front':
        print(front())
    elif m == 'back':
        print(back())
