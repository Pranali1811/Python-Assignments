import schedule
import time
from datetime import datetime

def log_timestamp():
    filename = "Marvellous.txt"
   
    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    log_entry = f"Task executed at: {current_time}\n"
    
    try:
        
        with open(filename, 'a') as file:
            file.write(log_entry)
            print(f"Logged to {filename}: Task executed at: {current_time}")
    except Exception as e:
        print(f"An error occurred: {e}")

schedule.every(5).minutes.do(log_timestamp)

if __name__ == "__main__":
    print("Scheduler started. Logging every 5 minutes to Marvellous.txt. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)