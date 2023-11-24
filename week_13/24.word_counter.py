# 단어 카운터 만들기
from collections import Counter

text_data = 'Create the highest, grandest vision possible for your life, because you become what you believe'

a = Counter(text_data.split())

print(a)
