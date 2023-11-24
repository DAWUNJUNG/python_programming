# 학생 성적 처리
def main():
    address_book = {}
    while True:
        user = display_menu()
        if user == 1:
            name, number = get_contact()
            address_book[name] = number
        elif user == 2:
            name, number = get_contact()
            address_book.pop(name)
        elif user == 3:
            pass  # 도전 문제 참조
        elif user == 4:
            for key in sorted(address_book):
                print(key, '의 전화번호:', address_book[key])
        else:
            break


# 이름과 전화번호를 입력받아서 반환한다. 
def get_contact():
    name = input('이름: ')
    number = input('전화번호:')
    return name, number  # 튜플로 반환한다. 


def display_menu():
    print('1. 연락처 추가')
    print('2. 연락처 삭제')
    print('3. 연락처 검색')
    print('4. 연락처 출력')
    print('5. 종료')
    select = int(input('메뉴 항목을 선택하시오: '))
    return select


main()