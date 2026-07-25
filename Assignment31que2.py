import schedule
import time

def DisplayMessage(message):
    print(message)

def main():
  
    user_message = input("Enter message to schedule: ").strip()

   
    schedule.every(5).seconds.do(DisplayMessage, message=user_message)

    print(f"\nScheduled 'DisplayMessage' every 5 seconds. Press Ctrl+C to stop.\n")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()