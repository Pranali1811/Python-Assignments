import os

def search_word_in_file(filename, word):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return

    try:
        with open(filename, 'r') as file:
            content = file.read()
 
            words = content.split()
            
            if word in words:
                print(f"The word '{word}' is present in {filename}.")
            else:
                print(f"The word '{word}' is NOT present in {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    user_input = input("Enter file name and search word: ").split()
    
    if len(user_input) >= 2:
        file_name = user_input[0]
        target_word = user_input[1]
        search_word_in_file(file_name, target_word)
    else:
        print("Error: Please provide both the file name and the word to search.")