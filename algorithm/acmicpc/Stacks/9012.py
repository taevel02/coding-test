for _ in range(int(input())):
    ps = list(input())

    while len(ps) != 0:
        if ps[0] == ')':
            print("NO")
            break
        else:
            if ')' in ps:
                ps.remove(')')
                ps.remove('(')
            else:
                print("NO")
                break

    if len(ps) == 0:
        print("YES")
