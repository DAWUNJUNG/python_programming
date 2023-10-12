weight = float(input("무게(킬로그램): "))
height = float(input("키(미터): "))

bmi = weight / height ** 2

print("당신의 BMI:", bmi)

if bmi >= 20.0 and bmi < 25.0 :
    print("정상입니다.")
elif bmi >= 25.0 and bmi < 30.0 :
    print("과체중입니다.")
elif bmi >= 30.0 :
    print("비만입니다.")