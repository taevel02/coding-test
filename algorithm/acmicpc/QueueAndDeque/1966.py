for _ in range(int(input())):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))

    s_ = [0 for _ in range(n)]
    s_[m] = 1
    count = 0

    while True:
        if s[0] == max(s):
            count += 1
            if s_[0] == 1:
                print(count)
                break
            else:
                del s[0]
                del s_[0]
        else:
            s.append(s[0])
            del s[0]
            s_.append(s_[0])
            del s_[0]
