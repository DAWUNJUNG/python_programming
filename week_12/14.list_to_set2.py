# 리스트 <-> 세트
list1 = [1, 2, 3, 4, 5, 1, 2, 4]
len(set(list1))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
set(list1) & set(list2)
