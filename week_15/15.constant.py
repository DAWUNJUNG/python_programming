# 상수 정의
class Monster:
    # 상수 값 정의
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERYSTRONG = 30

    def __init__(self):
        self._health = Monster.NORMAL

    def eat(self):
        self._health = Monster.STRONG

    def attack(self):
        self._health = Monster.WEAK
