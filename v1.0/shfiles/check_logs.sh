#!/bin/bash

# Define the log directory and the output ptl file
LOG_DIR="../logs"
OUTPUT_FILE="error_report.ptl"

# List of error keywords to search for
errors=("Error" "ERROR" "error")

# Create or clear the output file
> "$OUTPUT_FILE"

# Loop through each log file in the directory
for log_file in "$LOG_DIR"/*
do
    if [ -f "$log_file" ]; then
        line_num=1
        while IFS= read -r line
        do
            for error in "${errors[@]}"
            do
                if [[ "$line" == *"$error"* ]]; then
                    echo "$log_file: Line $line_num: $line" >> "$OUTPUT_FILE"
                fi
            done
            ((line_num++))
        done < "$log_file"
    fi
done

echo "Error report generated in $OUTPUT_FILE"
