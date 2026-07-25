import os

def check_file_exists(filename):
    if os.path.exists(filename):
        print(f"File '{filename}' exists in current directory.")
    else:
        print(f"File '{filename}' does NOT exist in current directory.")

if __name__ == "__main__":
    file_name = input("Enter file name: ")
    check_file_exists(file_name)