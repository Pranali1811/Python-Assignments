import os
import shutil
import schedule
import time
from datetime import datetime

def copy_txt_files(src_dir, dest_dir):
  
    if not os.path.exists(src_dir) or not os.path.isdir(src_dir):
        print(f"Error: Source directory '{src_dir}' is invalid or does not exist.")
        return

    if not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir, exist_ok=True)
            print(f"Created destination directory: '{dest_dir}'")
        except Exception as e:
            print(f"Error creating destination directory: {e}")
            return

    log_filename = "CopyLog.txt"
    timestamp = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    print(f"\n--- Starting .txt file copy job [{timestamp}] ---")

    try:
        files = os.listdir(src_dir)
    except Exception as e:
        print(f"Error listing source directory: {e}")
        return

    for file_name in files:

        if file_name.endswith(".txt"):
            src_file_path = os.path.join(src_dir, file_name)
            dest_file_path = os.path.join(dest_dir, file_name)

           
            if os.path.isfile(src_file_path):
                
                try:
                    shutil.copy(src_file_path, dest_file_path)
                    log_entry = f"[{timestamp}] Successfully copied: {file_name} -> {dest_dir}\n"
                    print(f"Copied: {file_name}")

                except Exception as e:
                    log_entry = f"[{timestamp}] Failed to copy: {file_name}. Error: {e}\n"
                    print(f"Failed to copy {file_name}: {e}")

               
                with open(log_filename, 'a') as log_file:
                    log_file.write(log_entry)

if __name__ == "__main__":
    source_dir = input("Enter source directory path: ").strip()
    destination_dir = input("Enter destination directory path: ").strip()

 
    schedule.every(10).minutes.do(copy_txt_files, source_dir, destination_dir)

    print("\nCopy scheduler started. Copying .txt files every 10 minutes. Press Ctrl+C to stop.\n")
    
    
    copy_txt_files(source_dir, destination_dir)

    while True:
        schedule.run_pending()
        time.sleep(1)