import os

def display_file_contents(filename):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("--- File Contents ---")
            print(content)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_name = input("Enter file name: ")
    display_file_contents(file_name)