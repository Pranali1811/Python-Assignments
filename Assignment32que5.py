import os
import schedule
import time
from datetime import datetime

def delete_empty_files(target_dir):
    if not os.path.exists(target_dir) or not os.path.isdir(target_dir):
        print(f"Error: Target directory '{target_dir}' is invalid or does not exist.")
        return

    log_filename = "DeletedFilesLog.txt"
    timestamp = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    print(f"\n--- Scanning for empty files [{timestamp}] ---")

    
    for root, _, files in os.walk(target_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            try:
                
                if os.path.getsize(file_path) == 0:
                    os.remove(file_path)
                    
                    log_entry = f"[{timestamp}] Deleted empty file: {file_path}\n"
                    print(f"Deleted: {file_path}")

                    
                    with open(log_filename, 'a') as log_file:
                        log_file.write(log_entry)

            except PermissionError:
                error_msg = f"[{timestamp}] Permission denied: Could not delete {file_path}\n"
                print(f"Permission Error: {file_path}")
                with open(log_filename, 'a') as log_file:
                    log_file.write(error_msg)

            except Exception as e:
                error_msg = f"[{timestamp}] Error deleting {file_path}: {e}\n"
                print(f"Error processing {file_path}: {e}")
                with open(log_filename, 'a') as log_file:
                    log_file.write(error_msg)

if __name__ == "__main__":
    directory = input("Enter directory path to scan (use a sample folder for testing): ").strip()

   
    schedule.every(1).hours.do(delete_empty_files, directory)

    print("\nEmpty file cleanup scheduler started. Running every hour. Press Ctrl+C to stop.\n")
    
    
    delete_empty_files(directory)

    while True:
        schedule.run_pending()
        time.sleep(1)