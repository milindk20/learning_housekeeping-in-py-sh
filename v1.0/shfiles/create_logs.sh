#!/bin/bash

# Define the log directory
LOG_DIR="../logs"

# Check if the log directory exists, if not, create it
if [ ! -d "$LOG_DIR" ]; then
    mkdir -p "$LOG_DIR"
fi

# Array of possible error messages
errors=("Error" "ERROR" "error")

# Loop to create 100 log files
for i in {1..100}
do
    # Define the log file name with a timestamp and index
    LOG_FILE="$LOG_DIR/log_$(date +'%Y%m%d_%H%M%S')_$i.txt"

    # Create the log file
    touch "$LOG_FILE"

    # Write a message to the log file
    echo "Log file number $i created at $(date)" >> "$LOG_FILE"

    # Randomly decide whether to include an error message
    if [ $((RANDOM % 2)) -eq 0 ]; then
        # Select a random error message
        error_message=${errors[$RANDOM % ${#errors[@]}]}
        echo "$error_message occurred in log file number $i" >> "$LOG_FILE"
    fi

    # Print a message to the console
    echo "Log file created: $LOG_FILE"

    # Sleep for a second to ensure unique timestamps
    #sleep 1
done
