# 생성자
class Counter:
    def __init__(self, iniValue=0):
        self.count = iniValue

    def increment(self):
        self.count += 1


a = Counter(100)
b = Counter()
