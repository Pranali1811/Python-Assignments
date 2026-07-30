import sys
import psutil

def display_specific_process(target_name):
   
    found = False
    print(f"{'PID':<10} {'Name':<30} {'Username':<20}")
    print("=" * 60)
    
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            info = proc.info
            process_name = info['name'] or ""
            
            if target_name.lower() in process_name.lower():
                found = True
                pid = info['pid']
                username = info['username'] or "N/A"
                print(f"{pid:<10} {process_name:<30} {username:<20}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if not found:
        print(f"No running process found with name: '{target_name}'")

def main():
    
    if len(sys.argv) != 2:
        print("Error: Please provide a process name.")
        print("Usage: python ProcInfoSearch.py <ProcessName>")
        sys.exit(1)

    process_name = sys.argv[1]
    display_specific_process(process_name)

if __name__ == "__main__":
    main()