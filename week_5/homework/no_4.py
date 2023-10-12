circleHalf = int(input('원의 반지름: '))

if circleHalf < 0:
    print('잘못된 값입니다')

circleArea = (circleHalf ** 2) * 3.14

print(circleArea)