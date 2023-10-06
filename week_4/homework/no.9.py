number = int(input("정수="))

sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number = number // 10

print(sum_of_digits)