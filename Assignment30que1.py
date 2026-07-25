import schedule
import time

def job():
    print("Jay Ganesh...")


schedule.every(2).seconds.do(job)

if __name__ == "__main__":
    print("Program started. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)