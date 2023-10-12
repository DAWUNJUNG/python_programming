char = input('문자를 입력하시오: ')

printWord = ''

if char.lower() == 'r':
    printWord = 'Rectangle'
elif char.lower() == 't':
    printWord = 'Triangle'
elif char.lower() == 'c':
    printWord = 'Circle'

print(printWord)