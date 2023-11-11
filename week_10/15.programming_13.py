arr_1 = []
for i in range(9):
    arr_1.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


def booking():
    print("======================================")
    print("0 1 2 3 4 5 6 7 8 9 10")
    print("======================================")
    for i in arr_1:
        print(i)
    print("")


def check():
    row = int(input("원하시는 좌석의 행번호를 입력하세요(종료는 –1)"))
    column = int(input("원하시는 좌석의 열번호를 입력하세요(종료는 –1)"))

    if arr_1[row][column] == 1:
        print("이미 예약된 자리입니다.")
    else:
        print("예약합니다.")
        arr_1[row][column] = 1


booking()
check()
booking()
