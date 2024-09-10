#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""

import sys

# Initialize counters and total size
total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
count = 0

def print_stats():
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

try:
    for line in sys.stdin:
        count += 1
        # Split the line and try to extract relevant information
        tokens = line.split()
        if len(tokens) > 6:
            # Extract file size and status code
            file_size = int(tokens[-1])
            status_code = tokens[-2]
            
            # Update total file size
            total_size += file_size
            
            # Update status code counts if valid
            if status_code in status_codes:
                status_codes[status_code] += 1
        
        # Print every 10 lines
        if count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats when interrupted
    print_stats()
    raise

# Final print after the loop finishes
print_stats()
