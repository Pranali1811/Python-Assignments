import schedule
import time

def job():
    print("Coding Kar..!")


schedule.every(30).minutes.do(job)

if __name__ == "__main__":
    print("Scheduler started. Running every 30 minutes. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)