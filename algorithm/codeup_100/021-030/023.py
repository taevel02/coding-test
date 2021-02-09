n = input()
check = 10000

for i in range(5):
    print("[%d]" % (int(n[i])*check))
    check /= 10
