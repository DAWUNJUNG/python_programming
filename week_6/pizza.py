def main():
    print(f"20cm 피자 2개의 면적:{get_area(20) + get_area(20)}")
    print(f"30cm 피자 1개의 면적:{get_area(30)}")

def get_area(radius):
    if radius > 0:
        area = 3.14 * radius ** 2
    else:
        area = 0
    return area

main()