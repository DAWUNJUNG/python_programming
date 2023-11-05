squares = []

for x in range(10):
    squares.append(x*x)

# 기말고사 내기 딱 좋은 문제
squares = [x*x for x in range(10) if x % 2 == 0]

prices = [135, -545, 922, 356, -992, 217]
mprices = [i if i > 0 else 0 for i in prices]
print(mprices)

words = ["All", "good", "things", "must", "come", "to", "an", "end."]
letters = [ w[0] for w in words ]
print(letters)

numbers = [x+y for x in ['a','b','c'] for y in ['x','y','z']]
print(numbers)


