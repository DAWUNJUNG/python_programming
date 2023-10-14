def main():
    result1 = get_area(3)
    print('반지름이 3인 원의 면적=', result1)

def get_area(redius):
    area = 3.14 * redius ** 2
    return area

main()