drive_name = input("드라이브 이름: ")
directory_name = input("디렉토리 이름: ")
file_name = input("파일 이름: ")
extension = input("확장자: ")

full_file_name = drive_name + ':' + directory_name + file_name + '.' + extension

print("완전한 이름은", full_file_name)