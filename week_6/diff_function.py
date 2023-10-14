def get_area(radius):
    area = 3.14 * radius ** 2
    return area

result = get_area(3)
result2 = get_area(20)
print(f"반지름이 3인 원의 면적={result}")
print(f"반지름이 20인 원의 면적={result2}")