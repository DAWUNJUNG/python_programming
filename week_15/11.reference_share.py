# 참조 공유
class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def setChannel(self, channel):
        self.channel = channel


t = Television(11, 10, True)
s = t
s.channel = 9

# is, is not
if s is t:
    print("2개의 변수는 동일한 객체를 참조하고 있습니다.")

if s is not t:
    print("2개의 변수는 다른 객체를 참조하고 있습니다.")
