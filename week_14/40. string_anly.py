# 문자열 분석
import re

sentence = input("문자열을 입력하시오: ")

table = {"alphas": 0, "digits": 0, "spaces": 0}

for i in sentence:
    if re.compile('[a-zA-Zㄱ-ㅎㅏ-ㅣ가-힣]').match(i):
        table["alphas"] += 1
    if re.compile('[0-9]').match(i):
        table["digits"] += 1
    if re.compile('\s').match(i):
        table["spaces"] += 1

print(table)
