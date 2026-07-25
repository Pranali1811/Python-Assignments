import sys
import os

def copy_file_cmd():
    
    if len(sys.argv) < 2:
        print("Error: Please provide the source file name as a command-line argument.")
        print("Usage: python script.py <SourceFileName>")
        return

    source_filename = sys.argv[1]
    destination_filename = "Demo.txt"

    if not os.path.exists(source_filename):
        print(f"Error: Source file '{source_filename}' does not exist.")
        return

    try:
        with open(source_filename, 'r') as src, open(destination_filename, 'w') as dest:
            dest.write(src.read())
            print(f"Successfully created '{destination_filename}' and copied contents of '{source_filename}' into it.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    copy_file_cmd()