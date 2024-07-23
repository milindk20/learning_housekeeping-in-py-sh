import os
from datetime import datetime
import time
import random

# Define the log directory
LOG_DIR = "../logs"

# Check if the log directory exists, if not, create it
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Possible error messages
errors = ["Error", "ERROR", "error"]

# Loop to create 100 log files
for i in range(1, 101):
    # Define the log file name with a timestamp and index
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = os.path.join(LOG_DIR, f'log_{timestamp}_{i}.txt')

    # Create the log file and write a message to it
    with open(log_file, 'w') as f:
        f.write(f'Log file number {i} created at {datetime.now()}\n')

        # Randomly decide whether to include an error message
        if random.choice([True, False]):
            f.write(f'{random.choice(errors)} occurred in log file number {i}\n')

    # Print a message to the console
    print(f'Log file created: {log_file}')

    # Sleep for a second to ensure unique timestamps
    #time.sleep(1)
