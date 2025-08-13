from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


def tests():
    first_test = get_file_content("calculator", "lorem.txt")
    print(first_test)

if __name__ == "__main__":
    tests()