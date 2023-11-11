arr = ['aba', 'xyz', 'abc', '121']
print(arr)

count = 0
for i in arr:
    if i[0] == i[-1]:
        count += 1

print('문자열의 개수=', count)