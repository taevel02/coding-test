import sys
x, y = map(int, sys.stdin.readline().split())

week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
daySum = 0

for i in range(1, x):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        daySum += 31
    elif i == 2:
        daySum += 28
    else:
        daySum += 30

daySum += y
print(week[daySum % 7])
