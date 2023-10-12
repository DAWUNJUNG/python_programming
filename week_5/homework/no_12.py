year = int(input('연도를 입력하시오: '))

beltNum = year % 12

beltName = ''

if beltNum == 0:
    beltName = '원숭이'
elif beltNum == 1:
    beltName = '닭'
elif beltNum == 2:
    beltName = '개'
elif beltNum == 3:
    beltName = '돼지'
elif beltNum == 4:
    beltName = '쥐'
elif beltNum == 5:
    beltName = '소'
elif beltNum == 6:
    beltName = '호랑이'
elif beltNum == 7:
    beltName = '토끼'
elif beltNum == 8:
    beltName = '용'
elif beltNum == 9:
    beltName = '뱀'
elif beltNum == 10:
    beltName = '말'
elif beltNum == 11:
    beltName = '양'

print(f"{beltName}띠입니다.")
