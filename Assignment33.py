# ============================================================
# Duplicate File Removal Automation Using Python
# ============================================================

import sys
import os
import re
import time
import hashlib
import smtplib

from datetime import datetime
from email.message import EmailMessage


# ============================================================
# 1. HELP OPTION
# ============================================================

def display_help():

    print("""
Duplicate File Removal Automation

This script:
1. Scans a directory recursively.
2. Finds duplicate files using SHA-256 checksum.
3. Keeps the first file.
4. Deletes remaining duplicate files.
5. Creates a timestamp-based log file.
6. Sends the log file through email.
7. Repeats the operation after the given interval.

Usage:

python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <IntervalInMinutes> <ReceiverEmail>

Example:

python DuplicateFileRemoval.py E:/Data/Demo 50 receiver@gmail.com

Options:

-h
--help

-u
--usage
""")


# ============================================================
# 2. USAGE OPTION
# ============================================================

def display_usage():

    print("""
Usage:

python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <IntervalInMinutes> <ReceiverEmail>

Example:

python DuplicateFileRemoval.py E:/Data/Demo 50 receiver@gmail.com
""")


# ============================================================
# 3. EMAIL VALIDATION
# ============================================================

def validate_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(pattern, email) is not None


# ============================================================
# 4. DIRECTORY VALIDATION
# ============================================================

def validate_directory(directory):

    if not directory:
        return False, "Directory path is not provided."

    if not os.path.isabs(directory):
        return False, "Directory path must be absolute."

    if not os.path.exists(directory):
        return False, "Directory does not exist."

    if not os.path.isdir(directory):
        return False, "Path is not a directory."

    if not os.access(directory, os.R_OK):
        return False, "Directory is not readable."

    if not os.access(directory, os.W_OK):
        return False, "Directory is not writable."

    return True, ""


# ============================================================
# 5. TIME INTERVAL VALIDATION
# ============================================================

def validate_interval(interval):

    try:

        value = int(interval)

        if value <= 0:
            return False, "Interval must be greater than zero."

        return True, value

    except ValueError:

        return False, "Interval must be a numeric value."


# ============================================================
# 6. SHA-256 CHECKSUM
# ============================================================

def calculate_checksum(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        while True:

            data = file.read(8192)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


# ============================================================
# 7. GET ALL FILES RECURSIVELY
# ============================================================

def get_all_files(directory, log_directory):

    file_list = []

    for root, dirs, files in os.walk(directory):

        # Do not scan Marvellous log directory
        dirs[:] = [
            d for d in dirs
            if os.path.abspath(
                os.path.join(root, d)
            ) != os.path.abspath(log_directory)
        ]

        for file_name in files:

            file_path = os.path.join(
                root,
                file_name
            )

            if os.path.isfile(file_path):

                file_list.append(file_path)

    return file_list


# ============================================================
# 8. FIND DUPLICATE FILES
# ============================================================

def find_duplicates(files, log_file):

    checksum_dictionary = {}

    duplicate_files = []

    for file_path in files:

        try:

            checksum = calculate_checksum(
                file_path
            )

            # First file with this checksum is kept
            if checksum not in checksum_dictionary:

                checksum_dictionary[checksum] = file_path

            # Other files are duplicates
            else:

                duplicate_files.append(
                    (file_path, checksum)
                )

        except PermissionError as error:

            log_file.write(
                f"ERROR: Permission denied: {file_path}\n"
            )

            log_file.write(
                f"Reason: {error}\n\n"
            )

        except OSError as error:

            log_file.write(
                f"ERROR: Cannot read file: {file_path}\n"
            )

            log_file.write(
                f"Reason: {error}\n\n"
            )

    return duplicate_files


# ============================================================
# 9. DELETE DUPLICATE FILES
# ============================================================

def delete_duplicates(
        duplicate_files,
        log_file):

    deleted_count = 0

    for file_path, checksum in duplicate_files:

        try:

            if os.path.isfile(file_path):

                os.remove(file_path)

                deleted_count += 1

                log_file.write(
                    "--------------------------------------------------\n"
                )

                log_file.write(
                    f"Deleted duplicate file:\n"
                )

                log_file.write(
                    f"{file_path}\n"
                )

                log_file.write(
                    f"Checksum: {checksum}\n\n"
                )

        except PermissionError as error:

            log_file.write(
                f"ERROR: Permission denied while deleting:\n"
            )

            log_file.write(
                f"{file_path}\n"
            )

            log_file.write(
                f"Reason: {error}\n\n"
            )

        except OSError as error:

            log_file.write(
                f"ERROR: Could not delete:\n"
            )

            log_file.write(
                f"{file_path}\n"
            )

            log_file.write(
                f"Reason: {error}\n\n"
            )

    return deleted_count


# ============================================================
# 10. CREATE LOG FILE
# ============================================================

def create_log_file():

    log_directory = os.path.join(
        os.getcwd(),
        "Marvellous"
    )

    os.makedirs(
        log_directory,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%d_%m_%Y_%H_%M_%S"
    )

    log_file_name = (
        "DuplicateRemovalLog_"
        + timestamp
        + ".log"
    )

    log_file_path = os.path.join(
        log_directory,
        log_file_name
    )

    return log_directory, log_file_path


# ============================================================
# 11. SEND EMAIL
# ============================================================

def send_email(
        receiver_email,
        log_file_path,
        start_time,
        completion_time,
        directory,
        total_files,
        duplicate_count,
        deleted_count,
        log_file):

    # Read credentials from environment variables
    sender_email = os.getenv(
        "MARVELLOUS_EMAIL"
    )

    sender_password = os.getenv(
        "MARVELLOUS_EMAIL_PASSWORD"
    )

    if not sender_email:

        log_file.write(
            "ERROR: MARVELLOUS_EMAIL is not configured.\n"
        )

        return False

    if not sender_password:

        log_file.write(
            "ERROR: MARVELLOUS_EMAIL_PASSWORD is not configured.\n"
        )

        return False

    try:

        message = EmailMessage()

        message["Subject"] = (
            "Duplicate File Removal Report"
        )

        message["From"] = sender_email

        message["To"] = receiver_email

        # Email body
        body = f"""
Jay Ganesh,

The duplicate-file removal operation
has been completed successfully.

Operation Statistics:

Starting time of scanning:
{start_time}

Completion time of scanning:
{completion_time}

Directory scanned:
{directory}

Total number of files scanned:
{total_files}

Total number of duplicate files found:
{duplicate_count}

Total number of duplicate files deleted:
{deleted_count}

Please find the detailed log file
attached to this email.

Regards,
Marvellous Automation System
"""

        message.set_content(body)

        # Attach log file
        with open(
            log_file_path,
            "rb"
        ) as file:

            file_data = file.read()

        message.add_attachment(
            file_data,
            maintype="text",
            subtype="plain",
            filename=os.path.basename(
                log_file_path
            )
        )

        # Gmail SMTP
        with smtplib.SMTP(
            "smtp.gmail.com",
            587
        ) as server:

            server.starttls()

            server.login(
                sender_email,
                sender_password
            )

            server.send_message(
                message
            )

        log_file.write(
            "Email delivery status: SUCCESS\n"
        )

        return True

    except Exception as error:

        log_file.write(
            "Email delivery status: FAILED\n"
        )

        log_file.write(
            f"Email Error: {error}\n"
        )

        return False


# ============================================================
# 12. VALIDATE COMMAND LINE ARGUMENTS
# ============================================================

def validate_arguments():

    # Help
    if len(sys.argv) == 2:

        if sys.argv[1] in [
            "-h",
            "--help"
        ]:

            display_help()

            return None

        # Usage
        if sys.argv[1] in [
            "-u",
            "--usage"
        ]:

            display_usage()

            return None

    # Required arguments
    if len(sys.argv) != 4:

        print(
            "Invalid number of arguments."
        )

        print(
            "Use --help for more information."
        )

        return False

    directory = sys.argv[1]

    interval = sys.argv[2]

    receiver_email = sys.argv[3]

    # Validate directory
    valid, message = validate_directory(
        directory
    )

    if not valid:

        print(message)

        return False

    # Validate interval
    valid, interval_result = validate_interval(
        interval
    )

    if not valid:

        print(interval_result)

        return False

    # Validate email
    if not validate_email(
        receiver_email
    ):

        print(
            "Invalid email address."
        )

        return False

    return (
        directory,
        interval_result,
        receiver_email
    )


# ============================================================
# 13. PERFORM ONE OPERATION
# ============================================================

def perform_operation(
        directory,
        receiver_email):

    start_datetime = datetime.now()

    start_time = start_datetime.strftime(
        "%d %B %Y, %I:%M:%S %p"
    )

    # Create log directory and log file
    log_directory, log_file_path = (
        create_log_file()
    )

    total_files = 0

    duplicate_count = 0

    deleted_count = 0

    completion_time = ""

    try:

        with open(
            log_file_path,
            "w",
            encoding="utf-8"
        ) as log_file:

            # Header
            log_file.write(
                "==================================================\n"
            )

            log_file.write(
                "       DUPLICATE FILE REMOVAL AUTOMATION\n"
            )

            log_file.write(
                "==================================================\n\n"
            )

            # Starting time
            log_file.write(
                f"Starting time of directory scanning:\n"
            )

            log_file.write(
                f"{start_time}\n\n"
            )

            # Directory
            log_file.write(
                f"Name of directory scanned:\n"
            )

            log_file.write(
                f"{directory}\n\n"
            )

            # Get files
            files = get_all_files(
                directory,
                log_directory
            )

            total_files = len(files)

            log_file.write(
                f"Total number of files scanned: "
                f"{total_files}\n\n"
            )

            # Find duplicates
            duplicate_files = find_duplicates(
                files,
                log_file
            )

            duplicate_count = len(
                duplicate_files
            )

            log_file.write(
                f"Total number of duplicate files found: "
                f"{duplicate_count}\n\n"
            )

            # Delete duplicates
            deleted_count = delete_duplicates(
                duplicate_files,
                log_file
            )

            log_file.write(
                f"Total number of duplicate files deleted: "
                f"{deleted_count}\n\n"
            )

            # Completion time
            completion_datetime = datetime.now()

            completion_time = (
                completion_datetime.strftime(
                    "%d %B %Y, %I:%M:%S %p"
                )
            )

            log_file.write(
                f"Completion time of directory scanning:\n"
            )

            log_file.write(
                f"{completion_time}\n\n"
            )

            log_file.write(
                "==================================================\n"
            )

            log_file.write(
                "Operation completed.\n"
            )

            log_file.write(
                "==================================================\n\n"
            )

        # Send email
        with open(
            log_file_path,
            "a",
            encoding="utf-8"
        ) as log_file:

            send_email(
                receiver_email,
                log_file_path,
                start_time,
                completion_time,
                directory,
                total_files,
                duplicate_count,
                deleted_count,
                log_file
            )

        return True

    except Exception as error:

        try:

            with open(
                log_file_path,
                "a",
                encoding="utf-8"
            ) as log_file:

                log_file.write(
                    "\nERROR DURING EXECUTION:\n"
                )

                log_file.write(
                    f"{error}\n"
                )

        except Exception:
            pass

        return False


# ============================================================
# 14. MAIN FUNCTION
# ============================================================

def main():

    result = validate_arguments()

    # Help / Usage
    if result is None:
        return

    # Validation failed
    if result is False:
        return

    directory, interval, receiver_email = result

    # Run continuously
    while True:

        perform_operation(
            directory,
            receiver_email
        )

        # Convert minutes to seconds
        time.sleep(
            interval * 60
        )


# ============================================================
# 15. START PROGRAM
# ============================================================

if __name__ == "__main__":

    main()