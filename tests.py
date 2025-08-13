from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


def tests():
    first_test = get_file_content("calculator", "main.py")
    print(first_test)
    second_test = get_file_content("calculator", "pkg/calculator.py")
    print(second_test)
    third_test = get_file_content("calculator", "/bin/cat")
    print(third_test)
    fourth_test = get_file_content("calculator", "pkg/does_not_exist.py")
    print(fourth_test)

if __name__ == "__main__":
    tests()