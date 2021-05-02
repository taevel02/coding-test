import sys

result = [0 for _ in range(10001)]

for i in range(int(sys.stdin.readline())):
    result[int(sys.stdin.readline()) - 1] += 1

for i in range(len(result)):
    if result[i] != 0:
        for _ in range(result[i]):
            sys.stdout.write(f'{str(i + 1)}\n')
