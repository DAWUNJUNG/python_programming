import turtle
import random

# 원그리기
t = turtle.Turtle()
t.color("blue")
t.shape("arrow")
t.penup()
t.goto(-200, 100)
t2 = t.clone()
t2.color("red")
t2.shape("turtle")
t2.penup()
t2.goto(-200, -100)

t.goto(300, 60)
t.pendown()
t.circle(40)
t.penup()
t.goto(-200, 100)
t2.goto(300, -140)
t2.pendown()
t2.circle(40)
t2.penup()
t2.goto(-200, -100)


# 본격 게임 시작
t.pendown()
t2.pendown()
die = [1, 2, 3, 4, 5, 6]
for i in range(20):
    if t.pos() >= (300, 100):
        print("첫 번째 플레이어가 이겼습니다. ")
        break
    elif t2.pos() >= (300, -100):
        print("두 번째 플레이어가 이겼습니다. ")
        break
    else:
        t_turn = input("주사위를 던지려면 엔터키를 누르세요. ")
        die_outcome = random.choice(die)
        print("주사위 결과: ")
        print(die_outcome)
        print("진행 위치: ")
        print(20 * die_outcome)
        t.fd(20 * die_outcome)
        t2_turn = input("주사위를 던지려면 엔터키를 누르세요. ")
        d = random.choice(die)
        print("주사위 결과: ")
        print(d)
        print("진행 위치: ")
        print(20 * d)
        t2.fd(20 * d)

turtle.mainloop()
turtle.bye()