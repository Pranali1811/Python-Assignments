import os
import schedule
import time
from datetime import datetime

def read_and_display_file(file_path):
    print(f"\n--- Reading File Output [{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}] ---")
    

    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    try:
        
        if os.path.getsize(file_path) == 0:
            print(f"Warning: The file '{file_path}' is empty.")
            return

       
        with open(file_path, 'r') as file:
            content = file.read()
            print("File Contents:")
            print(content)

  
    except PermissionError:
        print(f"Error: Permission denied to access '{file_path}'.")

   
    except IOError as e:
        print(f"Error: File cannot be opened. ({e})")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    target_file = input("Enter path of the file to read: ").strip()

    schedule.every(1).minutes.do(read_and_display_file, target_file)

    print(f"\nScheduler started. Reading '{target_file}' every minute. Press Ctrl+C to stop.\n")
    
   
    read_and_display_file(target_file)

    while True:
        schedule.run_pending()
        time.sleep(1)