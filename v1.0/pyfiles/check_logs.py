import os

# Define the log directory and the output ptl file
LOG_DIR = "../logs"
OUTPUT_FILE = "error_report.ptl"

# List of error keywords to search for
errors = ["Error", "ERROR", "error"]

with open(OUTPUT_FILE, 'w') as report:
    # Loop through each log file in the directory
    for log_file in os.listdir(LOG_DIR):
        log_path = os.path.join(LOG_DIR, log_file)
        if os.path.isfile(log_path):
            with open(log_path, 'r') as file:
                lines = file.readlines()
                for line_num, line in enumerate(lines, start=1):
                    if any(error in line for error in errors):
                        report.write(f"{log_file}: Line {line_num}: {line}")

print(f"Error report generated in {OUTPUT_FILE}")
