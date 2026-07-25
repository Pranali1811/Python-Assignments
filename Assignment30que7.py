import os
import shutil
import schedule
import time
from datetime import datetime

def perform_backup(source_path, destination_dir):
    if not os.path.exists(source_path):
        print(f"Error: Source file '{source_path}' does not exist.")
        return


    os.makedirs(destination_dir, exist_ok=True)

    try:
       
        base_name, extension = os.path.splitext(os.path.basename(source_path))
        
        timestamp_fname = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        new_filename = f"{base_name}_{timestamp_fname}{extension}"
        
        destination_path = os.path.join(destination_dir, new_filename)
        
    
        shutil.copy(source_path, destination_path)
        
      
        timestamp_log = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        log_entry = f"Backup completed successfully at {timestamp_log}\n"
        
       
        with open("backup_log.txt", "a") as log_file:
            log_file.write(log_entry)
            
        print(f"Backup created: {new_filename}")
        print(f"Logged to backup_log.txt: {log_entry.strip()}")

    except Exception as e:
        print(f"An error occurred during backup: {e}")

if __name__ == "__main__":
    source_file = input("Enter source file path: ").strip()
    dest_directory = input("Enter destination directory path: ").strip()


    schedule.every(1).hours.do(perform_backup, source_file, dest_directory)

    print("\nBackup scheduler started. Running every hour. Press Ctrl+C to stop.")
    
  
    perform_backup(source_file, dest_directory)

    while True:
        schedule.run_pending()
        time.sleep(1)