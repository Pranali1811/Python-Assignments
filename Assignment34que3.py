import sys
import os
import time
import psutil

def create_process_log(dir_name):

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log_filename = f"ProcessLog_{timestamp}.log"
    log_path = os.path.join(dir_name, log_filename)

    try:
        with open(log_path, 'w', encoding='utf-8') as log_file:
            log_file.write("==================================================\n")
            log_file.write(f"Process Log Created At: {time.ctime()}\n")
            log_file.write("==================================================\n\n")
            log_file.write(f"{'PID':<10} {'Name':<30} {'Username':<20}\n")
            log_file.write("-" * 60 + "\n")

            for proc in psutil.process_iter(['pid', 'name', 'username']):
                try:
                    info = proc.info
                    pid = info['pid']
                    name = info['name'] or "N/A"
                    username = info['username'] or "N/A"
                    log_file.write(f"{pid:<10} {name:<30} {username:<20}\n")
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue

        print(f"Log file successfully created at: {log_path}")
    except Exception as e:
        print(f"Error creating log file: {e}")

def main():
    if len(sys.argv) != 2:
        print("Error: Directory name missing.")
        print("Usage: python ProcInfoLog.py <DirectoryName>")
        sys.exit(1)

    directory = sys.argv[1]
    create_process_log(directory)

if __name__ == "__main__":
    main()