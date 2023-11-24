# 문자열의 공통 문자
s1 = input('첫 번째 문자열:')
s2 = input('두 번째 문자열:')

list1 = list(set(s1) & set(s2))

print('\n공통적인 글자:', end=' ')
for i in list1:
    print(i, end=' ')

txt = input('입력 텍스트: ')
words = txt.split(' ')
unique = set(words)

print('사용된 단어의 개수= ', len(unique))
print(unique)
