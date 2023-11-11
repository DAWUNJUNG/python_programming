ori_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(ori_list)):
    if 3 <= i <= 8:
        ori_list[i] = int('-' + str(ori_list[i]))

print(ori_list)