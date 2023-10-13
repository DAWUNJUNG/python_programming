ph = float(input('pH를 입력하시오: '))

if (ph < 7):
    print('산')
elif (ph > 7):
    print('알칼리')
else:
    print('중성')