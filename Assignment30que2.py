from datetime import datetime
import time

def display_current_time():
    while True:
       
        now = datetime.now()
        formatted_time = now.strftime("%d-%m-%Y %I:%M:%S %p")
        print(f"Current Date and Time: {formatted_time}")
        
       
        time.sleep(60)

if __name__ == "__main__":
    print("Program started. Press Ctrl+C to stop.")
    display_current_time()