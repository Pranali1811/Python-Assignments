import os

def copy_file(source_filename, destination_filename):
    if not os.path.exists(source_filename):
        print(f"Error: The source file '{source_filename}' does not exist.")
        return

    try:
        with open(source_filename, 'r') as src, open(destination_filename, 'w') as dest:
            content = src.read()
            dest.write(content)
            print(f"Successfully copied contents from '{source_filename}' to '{destination_filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
   
    user_input = input("Enter source file and destination file (separated by space): ").split()
    
    if len(user_input) >= 2:
        source_file = user_input[0]
        destination_file = user_input[1]
        copy_file(source_file, destination_file)
    else:
        print("Error: Please provide two file names.")