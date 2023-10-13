weight, tall = input('체중과 키를 입력하시오: ').split()

weight = int(weight)
tall = int(tall)

avg_weight = (tall - 100) * 0.9

if (avg_weight > weight):
    print('저체중입니다.')
elif (avg_weight < weight):
    print('과체중입니다.')
else:
    print('표준입니다.')