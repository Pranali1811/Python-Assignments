import schedule
import time
from datetime import datetime

def create_timestamped_file():
    now = datetime.now()

    
    timestamp_filename = now.strftime("%d_%m_%Y_%H_%M_%S")
    filename = f"File_{timestamp_filename}.txt"

   
    creation_date = now.strftime("%d-%m-%Y")
    creation_time = now.strftime("%I:%M:%S %p")

    try:
        with open(filename, 'w') as file:
            file.write(f"Filename: {filename}\n")
            file.write(f"Creation Date: {creation_date}\n")
            file.write(f"Creation Time: {creation_time}\n")

        print(f"File created successfully: {filename}")

    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

if __name__ == "__main__":
   
    schedule.every(1).minutes.do(create_timestamped_file)

    print("File generator started. Creating a new text file every minute. Press Ctrl+C to stop.")
    
   
    create_timestamped_file()

    while True:
        schedule.run_pending()
        time.sleep(1)