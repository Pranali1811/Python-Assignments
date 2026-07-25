import os

def count_string_frequency(filename, target_string):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return

    try:
        with open(filename, 'r') as file:
            content = file.read()
           
            frequency = content.count(target_string)
            print(f"The string '{target_string}' appears {frequency} times in {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    user_input = input("Enter file name and search string: ").split()
    
    if len(user_input) >= 2:
        file_name = user_input[0]
        search_string = user_input[1]
        count_string_frequency(file_name, search_string)
    else:
        print("Error: Please provide both the file name and the string to count.")