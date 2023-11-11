arr_a = [1, 2, 3, 4, 5]
arr_b = [1, 3, 3, 4, 5, 6, 7]

arr_result = []
for i in arr_a:
    for j in arr_b:
        if i == j and j not in arr_result:
            arr_result.append(i)

print('a=', arr_a)
print('b=', arr_b)
print()
print('결과=', arr_result)