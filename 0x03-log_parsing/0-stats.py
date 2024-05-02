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
    print('File size: {}'.format(total_file_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))


def process_logs():
    """Process log lines from stdin and compute statistics"""
    total_file_size = 0
    status_codes = {}
    lines_processed = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            lines_processed += 1

            if status_code in ['200', '301', '400',
                               '401', '403', '404', '405', '500']:
                total_file_size += file_size
                status_codes[status_code] = status_codes.get(
                    status_code, 0) + 1

                if lines_processed % 10 == 0:
                    print_statistics(total_file_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_codes)
        raise
    print_statistics(total_file_size, status_codes)


if __name__ == "__main__":
    process_logs()
