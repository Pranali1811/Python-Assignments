import schedule
import time
from datetime import datetime

def create_log_file():
    now = datetime.now()

   
    filename_time = now.strftime("%d_%m_%Y_%H_%M_%S")
    log_filename = f"MarvellousLog_{filename_time}.txt"

  
    content_time = now.strftime("%d-%m-%Y %I:%M:%S %p")

    try:
        with open(log_filename, 'w') as file:
            file.write("Log file created successfully.\n")
            file.write(f"Creation Time: {content_time}\n")

        print(f"Created log file: {log_filename}")

    except Exception as e:
        print(f"An error occurred while creating log file: {e}")

if __name__ == "__main__":
   
    schedule.every(10).minutes.do(create_log_file)

    print("Log creator started. Generating a new file every 10 minutes. Press Ctrl+C to stop.")
    
    
    create_log_file()

    while True:
        schedule.run_pending()
        time.sleep(1)