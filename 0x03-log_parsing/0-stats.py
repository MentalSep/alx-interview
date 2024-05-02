#!/usr/bin/python3
"""script that Process log lines from stdin and compute statistics"""
import sys


def print_stats(status_codes, file_size):
    """Print the total file size and number of lines by status code"""
    print('File size: {}'.format(file_size))
    for key, value in sorted(status_codes.items()):
        if value:
            print('{}: {}'.format(key, value))


total_file_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
    }
lines_processed = 0

try:
    for line in sys.stdin:
        args = line.split()

        if len(args) >= 7:
            file_size = int(args[-1])
            status_code = args[-2]

            if status_code in status_codes:
                status_codes[status_code] += 1

            total_file_size += file_size
            lines_processed += 1

            if lines_processed % 10 == 0:
                print_stats(status_codes, total_file_size)

except KeyboardInterrupt:
    print_stats(status_codes, total_file_size)
    raise
print_stats(status_codes, total_file_size)
