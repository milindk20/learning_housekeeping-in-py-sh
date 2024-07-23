import os
import time
import gzip
import shutil

# Define the log directory
LOG_DIR = "../logs"

# Define the time thresholds
GZIP_THRESHOLD_SECONDS = 5
DELETE_THRESHOLD_SECONDS = 60
# GZIP_THRESHOLD_DAYS = 5
# DELETE_THRESHOLD_DAYS = 30

# Get the current time
now = time.time()

# Loop through each file in the log directory
for log_file in os.listdir(LOG_DIR):
    log_path = os.path.join(LOG_DIR, log_file)
    
    if os.path.isfile(log_path):
        # Get the file's modification time
        file_mtime = os.path.getmtime(log_path)

        # Calculate the file age in seconds and days
        file_age_seconds = now - file_mtime
        file_age_days = file_age_seconds / (24 * 3600)

        # Gzip the file if it does not end with .gz and is older than the gzip threshold
        if not log_file.endswith('.gz') and file_age_seconds > GZIP_THRESHOLD_SECONDS:
            with open(log_path, 'rb') as f_in, gzip.open(log_path + '.gz', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            os.remove(log_path)
            print(f"Gzipped: {log_path}")

        # Delete the file if it ends with .gz and is older than the delete threshold
        if log_file.endswith('.gz') and file_age_seconds > DELETE_THRESHOLD_SECONDS:
            os.remove(log_path)
            print(f"Deleted: {log_path}")

        # Uncomment the following block for days-based housekeeping
        # if file_age_days > GZIP_THRESHOLD_DAYS and not log_file.endswith('.gz'):
        #     with open(log_path, 'rb') as f_in, gzip.open(log_path + '.gz', 'wb') as f_out:
        #         shutil.copyfileobj(f_in, f_out)
        #     os.remove(log_path)
        #     print(f"Gzipped: {log_path}")

        # if file_age_days > DELETE_THRESHOLD_DAYS and log_file.endswith('.gz'):
        #     os.remove(log_path)
        #     print(f"Deleted: {log_path}")

print("Housekeeping completed.")
