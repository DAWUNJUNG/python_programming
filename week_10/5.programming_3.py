list = [20, 1, 12, 9, 18]

for i in list:
    gondback = ''
    for j in range(6-len(str(i))):
        gondback += ' '
    print(i, end=gondback)

    for k in range(i):
        print('*', end='')
    print()