# 문자열 메소드: 찾기 및 바꾸기
s = input("파이썬 소스 파일 이름을 입력하시오: ")

if s.endswith(".py"):
    print("올바른 파일 이름입니다")
else:
    print("올바른 파일 이름이 아닙니다.")

s = "www.naver.com"
print(s.replace("com", "co.kr"))

s = "www.naver.co.kr"
print(s.find(".kr"))

s = "Let it be, let it be, let it be"
print(s.rfind("let"))

s = "www.naver.co.kr"
print(s.count("."))
