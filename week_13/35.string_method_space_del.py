# 문자열 메소드: 공백 제거
s = " Hello, World! "
print(s.strip())
s = "########this is example#####"
print(s.strip("#"))

s = "########this is example#####"
print(s.lstrip("#"))
print(s.rstrip("#"))