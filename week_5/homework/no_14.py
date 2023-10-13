import math

a = int(input('a를 입력하시오: '))
b = int(input('b를 입력하시오: '))
c = int(input('c를 입력하시오: '))

r = (b ** 2) - (4 * a * c)

answer1 = (-b - math.sqrt(r)) / (2 * a)
answer2 = (-b + math.sqrt(r)) / (2 * a)

if r < 1:
    print('실근이 없습니다.')
else:
    print(f"실근은 {answer1:.7f}과 {answer2:.7f}입니다.")