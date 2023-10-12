temperature = int(input('현재 온도를 입력하시오: '))
pants = ''

if temperature >= 25:
    pants = '반바지'
elif temperature < 25:
    pants = '긴바지'

print(f"{pants}를 추천합니다.")