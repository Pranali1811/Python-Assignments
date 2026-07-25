import schedule
import time

def job():
    print("Namskar...")


schedule.every().day.at("09:00").do(job)

if __name__ == "__main__":
    print("Scheduler started. Waiting for 09:00 AM daily. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)