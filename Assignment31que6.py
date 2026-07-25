import schedule
import time

def start_goals():
    print("Start your weekly goals")

def review_progress():
    print("Review your weekly progress")

def work_completed():
    print("Weekly work completed")


schedule.every().monday.at("09:00").do(start_goals)
schedule.every().wednesday.at("17:00").do(review_progress) 
schedule.every().friday.at("18:00").do(work_completed)     

if __name__ == "__main__":
    print("Weekly reminder scheduler started. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)