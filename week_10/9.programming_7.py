import random

arr_1 = []

for i in range(10):
    arr_1.append('a' + str(i))

print("list1=", arr_1)
print(random.choice(arr_1))