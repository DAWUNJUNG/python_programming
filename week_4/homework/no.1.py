x = int(input("x: "))
y = int(input("y: "))

sum_of_numbers = x + y
diff_of_numbers = x - y
product_of_numbers = x * y
average_of_numbers = (x + y) / 2

largest_number = max(x, y)
smallest_number = min(x, y)

print(f"두 수의 합: {sum_of_numbers}")
print(f"두 수의 차: {diff_of_numbers}")
print(f"두 수의 곱: {product_of_numbers}")
print(f"두 수의 평균: {average_of_numbers}")
print(f"큰 수: {largest_number}")
print(f"작은 수: {smallest_number}")