char = int(input(), 16)
for i in range(15):
    print('{:X}'.format(char) + '*' + '{:X}'.format(i+1) + '=' + '{:X}'.format(char * (i+1)))
