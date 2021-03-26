import sys
s = sys.stdin.readline()
arr = [-1 for _ in range(26)]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(s)):
    if s[i] in alphabet:
        idx = alphabet.index(s[i])
        if arr[idx] == -1:
            arr[idx] = i

for i in arr:
    print(i, end=' ')
