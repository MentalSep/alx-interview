#!/usr/bin/python3
""" Log parsing """
import sys
import re


def parse_line(line):
    """Parse a log line and extract relevant information"""
    parts = line.split()
    if len(parts) >= 7:
        status_code = parts[-2]
        file_size = int(parts[-1])
        return status_code, file_size
    return None, None


def print_statistics(total_file_size, status_codes):
    """Print the total file size and number of lines by status code"""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{:s}: {:d}".format(code, status_codes[code]))


def process_logs():
    """Process log lines from stdin and compute statistics"""
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
            status_code, file_size = parse_line(line)
            lines_processed += 1

            if status_code in status_codes:
                total_file_size += file_size
                status_codes[status_code] += 1

                if lines_processed % 10 == 0:
                    print_statistics(total_file_size, status_codes)

    except KeyboardInterrupt:
        pass
    print_statistics(total_file_size, status_codes)


if __name__ == "__main__":
    process_logs()
