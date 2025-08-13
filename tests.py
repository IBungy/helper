from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


def tests():
    first_test = run_python_file("calculator", "main.py")
    print(first_test)
    second_test = run_python_file("calculator", "main.py", ["3 + 5"])
    print(second_test)
    third_test = run_python_file("calculator", "tests.py")
    print(third_test)
    fourth_test = run_python_file("calculator", "../main.py")
    print(fourth_test)
    fifth_test = run_python_file("calculator", "nonexistent.py")
    print(fifth_test)

if __name__ == "__main__":
    tests()