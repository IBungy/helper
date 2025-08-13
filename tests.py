from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


def tests():
    first_test = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(first_test)
    second_test = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(second_test)
    third_test = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(third_test)


if __name__ == "__main__":
    tests()