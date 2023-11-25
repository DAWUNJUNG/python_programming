# 문자열은 불변 객체
word = "abcdef"
word[0]="A"

word = "abcdef"
word = "A" + word[1:]
print(word)
