# 하나의 클래스로 객체는 많이 만들 수 있다.
class Counter:
    def __init__(self, iniValue=0):
        self.count = iniValue

    def increment(self):
        self.count += 1


a = Counter(0)
b = Counter(100)