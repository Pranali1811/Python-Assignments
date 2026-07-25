import os

def count_words(filename):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return

    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            print(f"Total number of words in {filename}: {len(words)}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_name = input("Enter file name: ")
    count_words(file_name)