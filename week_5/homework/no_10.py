x = float(input('x의 값을 입력하시오: '))

fx = x ** 3

if x < 0:
    fx = (x ** 2) - (9 * x) + 2
else :
    fx = (7 * x) + 2

print(f"f(x)의 값은 {fx}")