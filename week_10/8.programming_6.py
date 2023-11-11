arr_1 = [1, 2, 3, 4, 5, 6]
arr_2 = [6, 7, 8, 9, 10]

print('list1=', arr_1)
print('list2=', arr_2)

bool_check = False

for i in range(len(arr_1)):
    for j in range(len(arr_2)):
        if arr_1[i] == arr_2[j]:
            bool_check = True

print(bool_check)