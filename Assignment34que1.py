import sys
import psutil

def display_all_processes():
    
    print(f"{'PID':<10} {'Name':<30} {'Username':<20}")
    print("=" * 60)
    
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            info = proc.info
            pid = info['pid']
            name = info['name'] or "N/A"
            username = info['username'] or "N/A"
            print(f"{pid:<10} {name:<30} {username:<20}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

def main():
    try:
        display_all_processes()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()