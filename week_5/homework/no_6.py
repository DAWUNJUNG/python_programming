import random

user = int(input('선택하시오(1: 가위 2:바위 3:보) '))

computer = random.randint(1,3)
print(f"컴퓨터의 선택(1: 가위 2:바위 3:보) {computer}")

if user == computer:
    print('비겼음')
elif user == 1:
    if computer == 3:
        print('사용자가 이겼음')
    elif computer == 2:
        print('컴퓨터가 이겼음')
elif user == 2:
    if computer == 3:
        print('사용자가 이겼음')
    elif computer == 1:
        print('컴퓨터가 이겼음')
elif user == 3:
    if computer == 1:
        print('사용자가 이겼음')
    elif computer == 2:
        print('컴퓨터가 이겼음')