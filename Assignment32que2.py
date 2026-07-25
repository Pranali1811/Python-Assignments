import os
import schedule
import time
from datetime import datetime

def monitor_file_size(file_path):
    log_filename = "FileSizeLog.txt"
    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

 
    if not os.path.exists(file_path):
        log_entry = (
            f"File Path: {file_path}\n"
            f"Status: File does not exist\n"
            f"Date and Time: {current_time}\n"
            "----------------------------------------\n"
        )
        print(f"Warning: File '{file_path}' does not exist. Logged status.")
    else:
        try:
          
            file_size = os.path.getsize(file_path)

            log_entry = (
                f"File Path: {file_path}\n"
                f"File Size: {file_size} bytes\n"
                f"Date and Time: {current_time}\n"
                "----------------------------------------\n"
            )
            print(f"Monitored '{file_path}' ({file_size} bytes). Details logged.")

        except Exception as e:
            print(f"An error occurred while checking file size: {e}")
            return

    try:
        with open(log_filename, 'a') as log_file:
            log_file.write(log_entry)
    except Exception as e:
        print(f"Failed to write to log file: {e}")

if __name__ == "__main__":
    target_file = input("Enter path of the file to monitor: ").strip()

  
    schedule.every(30).seconds.do(monitor_file_size, target_file)

    print(f"\nFile monitor started for '{target_file}' every 30 seconds. Press Ctrl+C to stop.\n")
    
  
    monitor_file_size(target_file)

    while True:
        schedule.run_pending()
        time.sleep(1)