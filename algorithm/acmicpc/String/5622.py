s = input()
sec = 0

for i in range(len(s)):
    if s[i] in ['A', 'B', 'C']:
        sec += 3
    elif s[i] in ['D', 'E', 'F']:
        sec += 4
    elif s[i] in ['G', 'H', 'I']:
        sec += 5
    elif s[i] in ['J', 'K', 'L']:
        sec += 6
    elif s[i] in ['M', 'N', 'O']:
        sec += 7
    elif s[i] in ['P', 'Q', 'R', 'S']:
        sec += 8
    elif s[i] in ['T', 'U', 'V']:
        sec += 9
    elif s[i] in ['W', 'X', 'Y', 'Z']:
        sec += 10

print(sec)
