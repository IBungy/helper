from functions import get_files_info



def tests():
    first_test = get_files_info("calculator", ".")
    print(f"Result for current directory:\n    {first_test}")
    second_test = get_files_info("calculator", "pkg")
    print(f"Result for 'pkg' directory:\n    {second_test}")
    third_test = get_files_info("calculator", "/bin")
    print(f"Result for '/bin' directory:\n    {third_test}")
    fourth_test = get_files_info("calculator", "../")
    print(f"Result for '../' directory:\n    {fourth_test}")

if __name__ == "__main__":
    tests()