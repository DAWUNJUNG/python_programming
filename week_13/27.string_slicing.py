# 문자열 슬라이싱
s = "Monty Python"
print(s[6:10])
print(s[:2])
print(s[4:])
print(s[:2] + s[2:])
print(s[:4] + s[4:])
print(s[:])

message="see you at noon"
low = message[:5]
high = message[5:]
print(low)
print(high)

reg= "980326"
print(reg[0:2]+"년")
print(reg[2:4]+"월")
print(reg[4:6]+"일")
