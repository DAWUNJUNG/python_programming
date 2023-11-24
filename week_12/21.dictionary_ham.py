# 딕셔너리 함축
values = [1, 2, 3, 4, 5, 6]

dic = {x: x ** 2 for x in values if x % 2 == 0}
print(dic)

dic = {i: str(i) for i in [1, 2, 3, 4, 5]}
print(dic)

fruits = ['apple', 'orange', 'banana']

dic = {f: len(f) for f in fruits}
print(dic)
