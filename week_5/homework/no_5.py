x, y, z = eval(input('3개의 정수를 입력하시오: '))
min = 0

if x > y :
    if y < z:
        min = y
    else :
        min = z
else:
    if x < z:
        min = x
    else :
        min = z


print(f"제일 작은 정수는 {min}입니다.")