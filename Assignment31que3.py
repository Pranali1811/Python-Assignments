import os
import schedule
import time
from datetime import datetime

def scan_directory(dir_path):
    if not os.path.exists(dir_path):
        print(f"Error: Directory '{dir_path}' does not exist.")
        return

    if not os.path.isdir(dir_path):
        print(f"Error: Path '{dir_path}' is not a valid directory.")
        return

    file_count = 0
    dir_count = 0

    try:
      
        for item in os.listdir(dir_path):
            full_path = os.path.join(dir_path, item)
            if os.path.isfile(full_path):
                file_count += 1
            elif os.path.isdir(full_path):
                dir_count += 1

        
        scan_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

        print("----------------------------------------")
        print(f"Directory Scanned: {dir_path}")
        print(f"Total Files: {file_count}")
        print(f"Total Subdirectories: {dir_count}")
        print(f"Scan Time: {scan_time}")
        print("----------------------------------------")

    except Exception as e:
        print(f"An error occurred while scanning: {e}")

if __name__ == "__main__":
    directory_to_scan = input("Enter directory path to scan: ").strip()

    
    schedule.every(1).minutes.do(scan_directory, directory_to_scan)

    print("\nDirectory scanner started. Running every minute. Press Ctrl+C to stop.")
    
    
    scan_directory(directory_to_scan)

    while True:
        schedule.run_pending()
        time.sleep(1)