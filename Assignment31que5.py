import os
import schedule
import time
from datetime import datetime

def log_directory_file_count(dir_path):
    if not os.path.exists(dir_path):
        print(f"Error: Path '{dir_path}' does not exist.")
        return

    if not os.path.isdir(dir_path):
        print(f"Error: '{dir_path}' is not a directory.")
        return

    try:
        
        file_count = 0
        for item in os.listdir(dir_path):
            full_path = os.path.join(dir_path, item)
            if os.path.isfile(full_path):
                file_count += 1

      
        timestamp = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        log_file_name = "DirectoryCountLog.txt"

     
        log_entry = (
            f"Directory Path: {dir_path}\n"
            f"Number of Files: {file_count}\n"
            f"Date and Time: {timestamp}\n"
            "----------------------------------------\n"
        )

      
        with open(log_file_name, "a") as log_file:
            log_file.write(log_entry)

        print(f"Logged details for '{dir_path}' into {log_file_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_directory = input("Enter directory path: ").strip()


    schedule.every(5).minutes.do(log_directory_file_count, target_directory)

    print("\nFile count logger started. Running every 5 minutes. Press Ctrl+C to stop.\n")
    
   
    log_directory_file_count(target_directory)

    while True:
        schedule.run_pending()
        time.sleep(1)