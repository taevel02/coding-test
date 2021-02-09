char = input()
t = 97
for _ in range(ord(char) - 96):
    print(chr(t))
    t += 1
