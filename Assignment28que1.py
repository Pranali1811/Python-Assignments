import os

def count_lines(filename):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return

    try:
        with open(filename, 'r') as file:
            line_count = len(file.readlines())
            print(f"Total number of lines in {filename}: {line_count}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_name = input("Enter file name: ")
    count_lines(file_name)