import os

def display_file_line_by_line(filename):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return

    try:
        with open(filename, 'r') as file:
            print(f"--- Contents of {filename} ---")
            for line in file:
                
                print(line, end='')
            print() 
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_name = input("Enter file name: ")
    display_file_line_by_line(file_name)