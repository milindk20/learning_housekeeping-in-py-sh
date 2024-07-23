#!/bin/bash

# Define the log directory
LOG_DIR="../logs"

# Define the time thresholds in seconds
GZIP_THRESHOLD_SECONDS=5
DELETE_THRESHOLD_SECONDS=60
# GZIP_THRESHOLD_DAYS=$((5*24*3600))
# DELETE_THRESHOLD_DAYS=$((30*24*3600))

# Get the current time
now=$(date +%s)

# Loop through each file in the log directory
for log_file in "$LOG_DIR"/*
do
    if [ -f "$log_file" ]; then
        # Get the file's modification time
        file_mtime=$(stat -c %Y "$log_file")

        # Calculate the file age in seconds
        file_age_seconds=$((now - file_mtime))

        # Gzip the file if it does not end with .gz and is older than the gzip threshold
        if [[ "$log_file" != *.gz && "$file_age_seconds" -gt "$GZIP_THRESHOLD_SECONDS" ]]; then
            gzip "$log_file"
            echo "Gzipped: $log_file"
        fi

        # Delete the file if it ends with .gz and is older than the delete threshold
        if [[ "$log_file" == *.gz && "$file_age_seconds" -gt "$DELETE_THRESHOLD_SECONDS" ]]; then
            rm "$log_file"
            echo "Deleted: $log_file"
        fi

        # Uncomment the following block for days-based housekeeping
        # if [[ "$log_file" != *.gz && "$file_age_seconds" -gt "$GZIP_THRESHOLD_DAYS" ]]; then
        #     gzip "$log_file"
        #     echo "Gzipped: $log_file"
        # fi

        # if [[ "$log_file" == *.gz && "$file_age_seconds" -gt "$DELETE_THRESHOLD_DAYS" ]]; then
        #     rm "$log_file"
        #     echo "Deleted: $log_file"
        # fi
    fi
done

echo "Housekeeping completed."
