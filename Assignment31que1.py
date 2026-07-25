import schedule
import time

def display_message(message):
    print(message)

def main():
    message = input("Enter message: ").strip()
    
    try:
        interval = int(input("Enter interval in seconds: ").strip())
        
  
        if interval <= 0:
            print("Error: The interval must be greater than zero.")
            return

        schedule.every(interval).seconds.do(display_message, message)

        print(f"\nScheduled to print '{message}' every {interval} seconds. Press Ctrl+C to stop.\n")

        while True:
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Error: Please enter a valid integer for seconds.")

if __name__ == "__main__":
    main()