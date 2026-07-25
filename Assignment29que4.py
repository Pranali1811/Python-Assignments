import sys
import os

def compare_files_cmd():
   
    if len(sys.argv) < 3:
        print("Error: Please provide two file names as command-line arguments.")
        print("Usage: python script.py <File1> <File2>")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if not os.path.exists(file1):
        print(f"Error: File '{file1}' does not exist.")
        return

    if not os.path.exists(file2):
        print(f"Error: File '{file2}' does not exist.")
        return

    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            if f1.read() == f2.read():
                print("Success")
            else:
                print("Failure")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    compare_files_cmd()